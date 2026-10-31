# A device-independent investigation workflow

1. Record model/SoC, Android/firmware, target APK origin and SHA-256. Keep the original signed APK as a control. Do not assume repackaging preserves native initialization.
2. Inventory public/access-controlled camera IDs, formats/sizes, advertised capabilities and request/result keys. Hidden provider entries are not extra physical cameras or proof of application access.
3. Establish preview and single-frame capture. Separate Java exceptions, native registration failures, stream configuration, conversion errors and blocked UI state.
4. Trace a small number of real frames at input/conversion/native boundaries. Compare numeric samples against packing and normalization metadata before tuning colors or curves.
5. Trace burst plan → actual submission → actual results → pixel timestamps → acceptance → final completion. Keep requested and actual values separate. Never rewrite actual metadata to make a failed plan appear valid.
6. Find a minimal supported capture strategy. Equal-exposure bursts may avoid unsupported transitions, but they are a compatibility experiment, not proof of full exposure bracketing.
7. Test repeated capture, cold start, scene-brightness changes, mode switches, front camera and moving subjects. Check image save, next-capture readiness and AE response separately.
8. Quantify image quality with repeated controls, matched actual exposures when possible, flat and textured targets, and original files. Report failures and processing time independently.
9. Add a device profile only after reproducible evidence. Protect model/Android/APK/input-specific overrides. An existing device profile must not activate on every Unisoc phone.

Start with [the capability schema](../schemas/device-report.schema.json) and the issue template. The included ADB collector gathers a small device summary and a redacted camera dump; it does not implement a standalone Camera2 manual-control test app. That remains a useful future contribution.

For exact known TYH212U hooks, read the [device repository](https://github.com/ChenQian-0701/gcam-tyh212u). For another device, inspect and validate each assumption rather than replacing a model string and shipping.
