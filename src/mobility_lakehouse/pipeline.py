from __future__ import annotations

import duckdb

from mobility_lakehouse.config import BRONZE_DIR, DATA_DIR, SQL_DIR, WAREHOUSE_PATH


def run_sql_file(connection: duckdb.DuckDBPyConnection, file_name: str) -> None:
    sql = (SQL_DIR / file_name).read_text()
    connection.execute(sql)


def run_pipeline() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    trips_path = BRONZE_DIR / "trips.csv"
    if not trips_path.exists():
        raise FileNotFoundError("Missing bronze trips file. Run `make generate` first.")

    with duckdb.connect(str(WAREHOUSE_PATH)) as connection:
        connection.execute(
            """
            create or replace table bronze_trips as
            select *
            from read_csv_auto(?);
            """,
            [str(trips_path)],
        )
        run_sql_file(connection, "silver_trips.sql")
        run_sql_file(connection, "gold_daily_metrics.sql")
        run_sql_file(connection, "gold_zone_metrics.sql")

    print(f"Built warehouse at {WAREHOUSE_PATH}")


if __name__ == "__main__":
    run_pipeline()

