# TYH212U case study: what generalizes

This is one device/firmware/APK case, not a survey proving support across Unisoc products. Detailed sources, configurations and evidence are maintained only in [gcam-tyh212u](https://github.com/ChenQian-0701/gcam-tyh212u).

| Observation in this case | Transferable investigation | Non-transferable parameter |
|---|---|---|
| Re-sign-only control lost native registration | Compare unmodified and re-signed controls | Exact BSG build/protection behavior |
| YUV→packed RAW10 samples saturated with mismatched levels | Inspect numeric samples and metadata together | Black=0, white=1023 |
| Alternating requested exposure did not match returned results | Associate requests/results/pixel timestamps | Fixed three-frame delay is not established |
| Same-exposure limited bursts produced repeated outputs | Establish a simpler controlled baseline | Six frames and camera-specific gains |
| Google AWB off removed tested purple cast | Single-variable input/output color controls | AWB=0 for all devices/light sources |
| A single-camera availability wait blocked readiness | Attribute the exact upstream state change | Rewrite every `[false]` on another device |
| AE reported ON but stopped responding after a shot | Measure actual exposure over scene changes | A generic AE-restart request was ineffective here |

The October 31 static-scene sample batch showed roughly 42–56% less output fluctuation in three flat laptop regions and stronger visible text/texture. It did not measure dynamic-range stops or merge weights. The underlying photos had no per-frame audit for that batch.

Full bracketing, standard-HDR repeatability and post-shot AE recovery remain incomplete. Keep successful controls and negative experiments together; a prior stage heading is not the current verdict.
