#!/usr/bin/env python3
from pathlib import Path
import base64

parts = [
    Path("bundle_parts/part001.txt"),
    Path("bundle_parts/part002.txt"),
    Path("bundle_parts/part003.txt"),
]
missing = [str(p) for p in parts if not p.exists()]
if missing:
    raise SystemExit("Missing parts: " + ", ".join(missing))

b64 = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
out = Path("reservation_dpo_th_20260401_bundle_fixed.tar.gz")
out.write_bytes(base64.b64decode(b64))
print(f"wrote {out}")
print("extract with: tar -xzf reservation_dpo_th_20260401_bundle_fixed.tar.gz")
