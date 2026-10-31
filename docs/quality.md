# Quantifying output improvements

Compare separately (a) real automatic mode behavior and (b) processing under matched actual frame exposure/ISO. HDR-off is still ISP/GCam-processed output, not a ground truth.

Use fixed camera/focus, stable nonflickering illumination, repeated original JPEGs, flat and textured targets. Inspect early exposure drift before selecting a stable subset; report all-sample sensitivity too. With known AE-recovery problems, independently verify recovery before each sample.

The included `compare_jpegs.py` uses explicit ROI boxes and computes per-pixel sample variance across captures. It reports the RMS temporal fluctuation, plus a variant subtracting each frame's brightness/linear-plane drift. Values use 8-bit encoded sRGB luminance coefficients. It performs **no registration**: motion or changed texture can dominate, so use small flat regions and inspect alignment. It does not undo ISP processing or local tone mapping.

`reduction = 1 - sigma_enhanced / sigma_off`

This is a change in output standard deviation, not overall image quality, sensor noise or algorithm participation percentage. Check material texture, halos, focus and fine low-contrast details alongside the flat-region result. Avoid quantization-floor estimators on heavily compressed/smoothed 8-bit images. Do not treat one mode as a reference for PSNR/SSIM quality ranking.

A dynamic-range gain in stops requires a calibrated scene/target, defined noise and contrast thresholds, and attention to local tone mapping. A compressed highlight or a brighter shadow alone is insufficient. HDR gain-map display rendering is a separate measurement domain from the SDR base JPEG.

An illustrative, device-specific dataset and its stronger registration/native-pixel sensitivity checks are documented in [the TYH212U quality report](https://github.com/ChenQian-0701/gcam-tyh212u/blob/main/docs/quality-results.md).

References: [Google HDR+ paper](https://research.google/pubs/burst-photography-for-high-dynamic-range-and-low-light-imaging-on-mobile-cameras/), [Imatest noise](https://www.imatest.com/imaging/noise/), [dynamic range](https://www.imatest.com/imaging/dynamic-range/), [Android Ultra HDR](https://developer.android.com/media/platform/hdr-image-format).
