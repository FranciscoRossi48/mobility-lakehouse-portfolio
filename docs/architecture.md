# Architecture

## Goal

Provide a portfolio-friendly data engineering project that runs locally at zero cost while mirroring patterns used in production analytics platforms.

## Layers

```text
data/bronze/trips.csv
        |
        v
bronze_trips
        |
        v
silver_trips
        |
        +--> gold_daily_metrics
        +--> gold_zone_metrics
        |
        v
Streamlit dashboard
```

## Components

- `extract.py` creates reproducible trip data.
- `pipeline.py` loads CSV data into DuckDB and runs SQL transformations.
- `sql/` contains transformation logic by layer.
- `tests/` validates data quality and pipeline behavior.
- `dashboard.py` reads gold and silver tables for exploration.
- `.github/workflows/ci.yml` runs lint, pipeline and tests on every push or pull request.

## Cost Control

This project intentionally avoids paid managed services. DuckDB provides local analytical storage, GitHub Actions provides free CI for public repositories, and Streamlit runs locally.

## Production Parallels

- DuckDB stands in for a cloud warehouse.
- CSV bronze files stand in for data lake object storage.
- SQL models stand in for dbt-style transformations.
- Pytest checks stand in for automated data quality gates.
- Streamlit stands in for a lightweight BI surface.
