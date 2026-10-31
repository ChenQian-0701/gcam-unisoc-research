# Reproducible evidence

For each experiment record: device profile, firmware, exact APK hash, source commit, preferences, runtime properties, capture mode, lighting/motion, repetitions, requested/actual frame values, native aborts, output filenames (locally), and recovery checks.

Use an A/B/A or randomized paired control and change one variable at a time. Capture current-process logs from the current experiment rather than relying on an overflowing historical log buffer. A missing log line is not proof a stage did not run.

Separate observations from hypotheses. State the test window and sample count. Do not call an observed 40-second stall permanent, a handful of saves long-term stability, or an experimental bracketed output a complete repair.

Before publication, allowlist the files to export, remove private identifiers/GPS/faces and review the result manually. Prefer small frame tables, selected key lines, aggregate metrics and permission-cleared crops. Keep a private source snapshot for traceability, not a public full property dump.
