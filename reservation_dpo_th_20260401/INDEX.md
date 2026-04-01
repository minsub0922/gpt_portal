# Reservation DPO artifacts

This directory contains the Thai reservation-extraction DPO artifacts prepared on 2026-04-01.

## Included

- A compressed bundle containing all generated datasets and scripts
- A restore helper script
- A small summary JSON

## Files

- `reservation_dpo_th_20260401_bundle.tar.gz.b64`: base64-encoded tar.gz bundle containing all generated artifacts
- `restore_bundle.py`: decodes the base64 file back to `reservation_dpo_th_20260401_bundle.tar.gz`
- `reservation_th_dpo_format_guard_summary.json`: summary of pair counts and negative-pattern focus

## Restore

```bash
python restore_bundle.py
tar -xzf reservation_dpo_th_20260401_bundle.tar.gz
```

After extraction, the bundle contains:

- `reservation_th_dpo_format_guard_train_1003.jsonl`
- `reservation_th_dpo_format_guard_eval_285.jsonl`
- `reservation_th_dpo_format_guard_pool_1288.jsonl`
- `reservation_th_sft_anchor_46.jsonl`
- `reservation_th_dpo_format_guard_summary.json`
- `build_reservation_dpo_dataset_v2.py`
- `train_dpo_notification_v2.py`
- `sanitize_reservation_output.py`
- `reservation_th_dpo_format_guard_README.md`
