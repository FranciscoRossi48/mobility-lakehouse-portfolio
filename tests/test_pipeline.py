import duckdb

from mobility_lakehouse.config import WAREHOUSE_PATH
from mobility_lakehouse.extract import main as extract_main
from mobility_lakehouse.pipeline import run_pipeline


def setup_module() -> None:
    extract_main()
    run_pipeline()


def test_expected_tables_exist() -> None:
    with duckdb.connect(str(WAREHOUSE_PATH), read_only=True) as connection:
        tables = {row[0] for row in connection.execute("show tables").fetchall()}

    assert {"bronze_trips", "silver_trips", "gold_daily_metrics", "gold_zone_metrics"} <= tables


def test_trip_ids_are_unique() -> None:
    with duckdb.connect(str(WAREHOUSE_PATH), read_only=True) as connection:
        duplicate_count = connection.execute(
            """
            select count(*)
            from (
                select trip_id
                from silver_trips
                group by trip_id
                having count(*) > 1
            )
            """
        ).fetchone()[0]

    assert duplicate_count == 0


def test_amounts_and_durations_are_valid() -> None:
    with duckdb.connect(str(WAREHOUSE_PATH), read_only=True) as connection:
        invalid_count = connection.execute(
            """
            select count(*)
            from silver_trips
            where total_amount < 0
               or fare_amount < 0
               or distance_km <= 0
               or duration_minutes <= 0
            """
        ).fetchone()[0]

    assert invalid_count == 0


def test_gold_tables_have_rows() -> None:
    with duckdb.connect(str(WAREHOUSE_PATH), read_only=True) as connection:
        daily_count = connection.execute("select count(*) from gold_daily_metrics").fetchone()[0]
        zone_count = connection.execute("select count(*) from gold_zone_metrics").fetchone()[0]

    assert daily_count > 0
    assert zone_count > 0

