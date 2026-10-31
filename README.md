# GCam on Unisoc: compatibility research

[简体中文](README.zh-CN.md) · [Porting guide](docs/porting-guide.md) · [Evidence rules](docs/evidence.md)

A methodology and tooling repository for investigating GCam compatibility on Unisoc / Spreadtrum Android devices. The initial case study is the China Telecom Tianyi One 2022 (TYH212U / ARES, UMS9620, Android 11).

**This repository provides research methods and read-only/offline tools. It contains no installable GCam, no universal hook module, and no claim of support for all Unisoc devices.**

The device-specific module, build/install instructions, settings and regression evidence live separately in [gcam-tyh212u](https://github.com/ChenQian-0701/gcam-tyh212u).

## What transfers across devices

- Establish accessible camera capabilities instead of inferring them from the SoC brand or hidden interface list.
- Trace input pixels and normalization metadata together; a synthetic RAW10 container is not sensor RAW.
- Associate native burst plans, submitted Camera2 requests, actual capture results, sensor timestamps and native completion.
- Distinguish frame acceptance, later consistency checks, image save, resource recovery and AE recovery.
- Keep repeatable controls, negative experiments, state snapshots and limited claims.

Read [architecture](docs/architecture.md), [porting workflow](docs/porting-guide.md), [failure modes](docs/failure-modes.md), and [the TYH212U case study](docs/case-studies/tyh212u.md).

## Included tools

```sh
python3 tools/collect_camera_info.py --out local-data/device
python3 tools/privacy/sanitize.py local-data/input.txt local-data/output.txt
python3 -m pip install -r requirements.txt
python3 tools/quality/compare_jpegs.py --off local-data/off --enhanced local-data/enhanced --rois examples/flat-rois.json --out local-data/metrics.json
python3 -m unittest discover -s tests -v
```

The collector is read-only and uses ADB. The sanitizer is best-effort; manually review every proposed upload. The quality tool expects fixed-camera, equal-size, orientation-normalized sRGB SDR images and explicit flat ROI coordinates. It does not register moving images, detect capture mode, infer merge weights, or measure sensor dynamic range. See [quality measurement](docs/quality.md).

## Status and contributions

Only TYH212U has a substantial case study so far. Help by contributing capability reports and reproducible experiments using the [issue template](.github/ISSUE_TEMPLATE/device-report.md). Research results, device profiles and working end-user ports are different deliverables.

Apache-2.0 applies to original project code/docs; see [third-party notices](THIRD_PARTY_NOTICES.md). GCam/BSG binaries and native processing libraries are not distributed or relicensed here.
