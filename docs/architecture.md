# Processing and compatibility boundaries

A typical native-RAW route starts with sensor Bayer data. The observed TYH212U route instead uses:

`Sensor → vendor ISP → YUV → BSG synthetic packed RAW10 conversion → native GCam processing → JPEG`

The converter already exists in the tested BSG build. The adapter corrects its inputs; it does not create hardware RAW support. A 10-bit container does not restore information clipped or denoised by an earlier stage.

Audit each boundary: actual image format, dimensions, row/pixel stride, packing, valid sample range, black/white levels, exposure and gains, shading/color/noise parameters, buffer ownership and release callbacks. Do not substitute plausible numbers without retaining the original values and a reversible control.

Exposure has several distinct representations: native plan, Java descriptors, submitted request, returned result and pixels. Correlate by tag, frame number and sensor timestamp where available. Manual control may be partial or delayed; an unsupported capability is not proof that every subfeature is impossible, and a submitted request is not proof that its settings took effect.

BSG obfuscated class names are version-specific. Hook implementations remain in the device repository; this repository records principles and reusable tools.
