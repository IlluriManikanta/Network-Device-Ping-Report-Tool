# Metrics Anomaly Detector (Python + Merlion)

A lightweight pipeline to ingest time-series system metrics (CSV or JSON), reshape them into a tidy long format, compute CPU utilization per core, and detect anomalies. Uses Salesforce **Merlion**’s standardized detector suite (e.g., Z-Score/Isolation Forest/Spectral Residual) to flag spikes, sustained drifts, and out-of-band behavior, then exports a compact JSON snapshot for dashboards or alerting.

## What it does
- **Ingest:** Reads Prometheus-style metrics with labels (e.g., `base_metric`, `cpu`, `instance`, `job`, `mode`) from CSV/JSON.
- **Transform:** Normalizes to long format with columns: `timestamp, value, base_metric, cpu, instance, job, mode`.
- **Utilization:** Computes CPU utilization per core over time (and can extend to other metrics present in the file).
- **Detect:** Runs a standardized anomaly detector suite via Merlion; outputs timestamps, scores, and severity.
- **Export:** Writes a lean JSON report (and optional CSV) for downstream use.

## Why it’s useful
- Turns messy metric dumps into analysis-ready data.
- Gives quick, explainable anomaly signals without wiring a full observability stack.
- Produces artifacts (CSV/JSON) that are easy to visualize or pipe into dashboards.

## Tech
- Python, pandas, numpy
- Merlion (Salesforce) for anomaly detection
- matplotlib for quick visuals (optional)

## Quick start
```bash
# 1) Install
pip install -r requirements.txt

# 2) Run (example)
python src/run_analysis.py \
  --input data/metrics.csv \
  --out-json output/anomalies.json \
  --out-csv output/long_metrics.csv \
  --enable-merlion
