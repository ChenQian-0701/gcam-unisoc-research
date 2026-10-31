# Failure modes and invalid shortcuts

| Observation | Investigate | It does not prove |
|---|---|---|
| Black preview after repackaging | Original vs re-signed control; native method registration; conversion | That the camera HAL cannot produce preview |
| Visible input but black JPEG | Numeric conversion range, black/white metadata, zero exposure and color/shading inputs | That all black images share one cause |
| `accepted=true` for payload frames | Later request consistency, dropped frame/base selection and final callback | That each frame received a nonzero merge weight |
| `Base frame -1` | Which frame was dropped and why; actual request/result mismatch | That forcing a base index repairs the input |
| JPEG saved, next capture blocked | Buffer/reference return, queues, gates and module state | That processing completed correctly |
| Centre spinner before any shot | Actual caller of readiness change, availability/session changes | That the last JPEG failed |
| AE mode reports ON but exposure frozen | Real exposure/ISO over scene changes and session lifecycle | That AE has resumed |
| More fine detail and more grain | Focus, sharpening, texture and random noise separately | That all high-frequency energy is real resolution |

Do not globally force UI ready, manufacture successful native return values, shift every result by a fixed frame offset, or apply sensor-RAW corrections to ISP-processed inputs without evidence. Some may be diagnostic experiments; they are not validated general repairs.
