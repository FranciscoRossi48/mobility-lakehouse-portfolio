# Portfolio Notes

## Problema

Equipos de operaciones necesitan entender demanda, ingresos y patrones de viajes por zona sin depender de herramientas pagas.

## Solucion

Un pipeline local que genera o ingiere viajes, los normaliza en DuckDB y publica metricas agregadas para analisis.

## Decisiones tecnicas

- DuckDB reemplaza un warehouse cloud para mantener costo cero.
- Python coordina la ingesta y el build.
- SQL mantiene las transformaciones legibles.
- Pytest valida reglas criticas de datos.
- GitHub Actions demuestra automatizacion sin infraestructura propia.

## Mejoras futuras

- Fuente real opcional desde datos abiertos.
- Dashboard local.
- Perfilado de datos.
- Documentacion de lineage.

