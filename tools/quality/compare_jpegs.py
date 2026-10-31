#!/usr/bin/env python3
"""Compare repeated, fixed-camera sRGB SDR JPEG outputs using explicit flat ROIs.

No mode detection, sensor SNR, HDR-display reconstruction or dynamic-range claim.
Use a tripod: this simple implementation performs no subpixel registration.
"""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
from PIL import Image,ExifTags

def measure(stack):
    h,w=stack.shape[1:];yy,xx=np.mgrid[-1:1:complex(h),-1:1:complex(w)]
    c=stack-stack.mean(axis=(1,2),keepdims=True)
    c=c-xx*np.mean(c*xx,axis=(1,2),keepdims=True)/np.mean(xx*xx)
    c=c-yy*np.mean(c*yy,axis=(1,2),keepdims=True)/np.mean(yy*yy)
    return {'mean':float(stack.mean()),
            'temporal_raw':float(np.sqrt(stack.var(axis=0,ddof=1).mean())),
            'temporal_plane_corrected':float(np.sqrt(c.var(axis=0,ddof=1).mean()))}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--off',type=Path,required=True);p.add_argument('--enhanced',type=Path,required=True)
    p.add_argument('--rois',type=Path,required=True,help='JSON mapping names to [left,top,right,bottom]')
    p.add_argument('--skip-first',type=int,default=0,help='Choose from metadata before inspecting quality outcomes')
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.skip_first<0:p.error('--skip-first must be nonnegative')
    rois=json.loads(a.rois.read_text());result={'domain':'8-bit sRGB SDR output','registration':'none; fixed camera required','skip_first':a.skip_first,'inventory':{},'regions':{}}
    common_size=None
    for mode,folder in [('off',a.off),('enhanced',a.enhanced)]:
        paths=sorted(x for x in folder.iterdir() if x.suffix.lower() in ['.jpg','.jpeg'])
        selected=paths[a.skip_first:]
        if len(selected)<3:p.error('At least 3 selected JPEGs per mode are required')
        stacks={n:[] for n in rois};inventory=[];expected_size=None
        for file in selected:
            with Image.open(file) as source:
                if source.getexif().get(274,1)!=1:p.error('Normalize EXIF orientation before comparison')
                im=source.convert('RGB');size=im.size
                if expected_size and size!=expected_size:p.error('Image sizes differ within group')
                if common_size and size!=common_size:p.error('Image sizes differ between groups')
                common_size=size
                expected_size=size
                ex=source.getexif().get_ifd(34665)
                row={'file':file.name,'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),
                     'size':size,'exposure_s':float(ex[33434]) if 33434 in ex else None,
                     'iso':int(ex[34855]) if 34855 in ex else None}
                inventory.append(row)
                for name,box in rois.items():
                    if not(0<=box[0]<box[2]<=size[0] and 0<=box[1]<box[3]<=size[1]):p.error('ROI outside image: '+name)
                    if box[2]-box[0]<2 or box[3]-box[1]<2:p.error('ROI needs at least two rows and columns')
                    rgb=np.asarray(im.crop(box),dtype=np.float64)
                    stacks[name].append(rgb@np.array([.2126,.7152,.0722]))
        result['inventory'][mode]=inventory
        for name,stack in stacks.items():result['regions'].setdefault(name,{})[mode]=measure(np.stack(stack))
    for name,groups in result['regions'].items():
        x=groups['off']['temporal_plane_corrected'];y=groups['enhanced']['temporal_plane_corrected']
        groups['standard_deviation_reduction_pct']=100*(1-y/x) if x else None
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
    print('Saved output statistics. Check actual exposure, focus, alignment and texture before drawing conclusions.')

if __name__=='__main__':main()
