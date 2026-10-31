#!/usr/bin/env python3
"""Best-effort log redaction. Always manually review before publishing."""
import argparse, ipaddress, re
from pathlib import Path

def sanitize(text, identifiers=()):
    for identifier in sorted(set(identifiers),key=len,reverse=True):
        if identifier: text=text.replace(identifier,'<REDACTED-ID>')
    text=re.sub(r'/(?:home|Users)/[^/\s\"\']+', '/home/USER', text)
    text=re.sub(r'\b(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b','<MAC>',text)
    def redact_ip(match):
        try: ipaddress.IPv4Address(match.group(0))
        except ipaddress.AddressValueError: return match.group(0)
        return '<IP>'
    text=re.sub(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])',redact_ip,text)
    text=re.sub(r'(?im)((?:imei|imsi|android[_ ]?id|serial(?:number|no)?|ssid|bssid|latitude|longitude|gpslatitude|gpslongitude|location)\s*[=:]\s*)[^\r\n,;]+',r'\1<REDACTED>',text)
    text=re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b','<EMAIL>',text)
    text=re.sub(r'\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b','<TOKEN>',text)
    return text

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input',type=Path);p.add_argument('output',type=Path)
    p.add_argument('--identifiers-file',type=Path,help='Local-only file, one private identifier per line')
    a=p.parse_args()
    if a.input.resolve()==a.output.resolve():p.error('Use a separate output; originals are not overwritten')
    ids=a.identifiers_file.read_text().splitlines() if a.identifiers_file else []
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(sanitize(a.input.read_text(errors='replace'),ids))
    print('Written redacted copy. Manually inspect names, faces, GPS and unlabelled identifiers.')

if __name__=='__main__': main()
