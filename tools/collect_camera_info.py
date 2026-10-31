#!/usr/bin/env python3
"""Collect a minimal read-only device summary and a locally redacted camera dump."""
import argparse,json,subprocess,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'privacy'))
from sanitize import sanitize

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--serial',help='ADB transport selection; not written to the report')
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();cmd=['adb']+(['-s',a.serial] if a.serial else [])
    def adb(*parts):return subprocess.run(cmd+list(parts),check=True,capture_output=True,text=True).stdout.strip()
    # adb rejects ambiguous multi-device selection; no arbitrary transport choice.
    private_serial=adb('get-serialno')
    fields={'model':'ro.product.model','device':'ro.product.device','platform':'ro.board.platform',
            'android':'ro.build.version.release','sdk':'ro.build.version.sdk'}
    report={key:adb('shell','getprop',prop) for key,prop in fields.items()}
    dump=adb('shell','dumpsys','media.camera')
    a.out.mkdir(parents=True,exist_ok=True)
    (a.out/'device.json').write_text(json.dumps(report,indent=2)+'\n')
    (a.out/'camera-dump.redacted.txt').write_text(sanitize(dump,[private_serial]))
    print('Read-only collection complete. Review the redacted dump before attaching it to an issue.')

if __name__=='__main__':main()
