#!/usr/bin/env python3
from pathlib import Path
import base64

src = Path('reservation_dpo_th_20260401_bundle.tar.gz.b64')
out = Path('reservation_dpo_th_20260401_bundle.tar.gz')
out.write_bytes(base64.b64decode(src.read_text()))
print(f"wrote {out}")
print("extract with: tar -xzf reservation_dpo_th_20260401_bundle.tar.gz")
