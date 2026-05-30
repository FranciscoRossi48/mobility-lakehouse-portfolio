# Mobility Lakehouse Portfolio

Proyecto de ingenieria de datos end-to-end, disenado para portfolio y para correr sin gastar un dolar.

Construye un mini lakehouse local con datos de viajes urbanos:

- Ingesta reproducible hacia una capa `bronze`.
- Transformaciones SQL hacia tablas `silver` y `gold`.
- Warehouse local en DuckDB.
- Tests de calidad de datos con `pytest`.
- Dashboard local con Streamlit.
- CI gratis con GitHub Actions.
- Documentacion clara para reclutadores y equipos tecnicos.

## Arquitectura

```text
Synthetic/public data
        |
        v
data/bronze/*.csv
        |
        v
DuckDB warehouse
        |
        +--> silver_trips
        +--> gold_daily_metrics
        +--> gold_zone_metrics
        +--> Streamlit dashboard
```

El proyecto funciona offline generando datos sinteticos. Eso evita costos, credenciales y dependencia de APIs pagas. Mas adelante se puede extender a fuentes publicas como NYC TLC Trip Record Data, OpenStreetMap o datasets abiertos de ciudades.

## Stack

- Python
- DuckDB
- Pandas
- Streamlit
- Pytest
- Ruff
- GitHub Actions

Todo corre local. No usa AWS, GCP, Azure, Snowflake, Databricks ni servicios pagos.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
make pipeline
make test
make dashboard
```

El pipeline crea:

- `data/bronze/trips.csv`
- `data/warehouse.duckdb`
- tablas analiticas dentro de DuckDB

Para inspeccionar resultados:

```bash
python -m mobility_lakehouse.query
```

Para abrir el dashboard:

```bash
make dashboard
```

## Comandos

```bash
make generate     # genera datos de ejemplo
make transform    # construye tablas silver/gold en DuckDB
make pipeline     # generate + transform
make dashboard    # abre un dashboard local
make test         # ejecuta tests
make lint         # ejecuta ruff
make clean        # borra artefactos generados
```

## Modelo de datos

### `silver_trips`

Tabla limpia a nivel viaje.

Campos principales:

- `trip_id`
- `pickup_ts`
- `dropoff_ts`
- `pickup_zone`
- `dropoff_zone`
- `passenger_count`
- `distance_km`
- `fare_amount`
- `tip_amount`
- `total_amount`
- `duration_minutes`

### `gold_daily_metrics`

Metricas agregadas por dia:

- cantidad de viajes
- ingresos totales
- distancia promedio
- tarifa promedio
- porcentaje promedio de propina

### `gold_zone_metrics`

Metricas por zona de origen:

- viajes
- ingresos
- distancia promedio
- duracion promedio

## Calidad de datos

Los tests validan:

- que el pipeline cree las tablas esperadas
- que no existan IDs duplicados
- que los montos no sean negativos
- que las duraciones sean positivas
- que las tablas gold tengan datos

## Como mostrarlo en portfolio

Este proyecto demuestra:

- modelado por capas tipo lakehouse
- SQL analitico
- automatizacion reproducible
- testing de datos
- CI/CD basico
- visualizacion de metricas en dashboard
- documentacion de arquitectura

Una buena descripcion para LinkedIn/GitHub:

> Built a zero-cost local data engineering lakehouse using Python, DuckDB, SQL, Streamlit, pytest and GitHub Actions. The pipeline ingests trip data, creates bronze/silver/gold layers, validates data quality and exposes analytics-ready metrics in a local dashboard.

## Roadmap gratis

- Agregar ingestion opcional desde datasets publicos.
- Agregar lineage simple con diagramas.
- Publicar capturas de queries y metricas en `/docs`.
- Agregar particionado por fecha para simular un data lake real.
