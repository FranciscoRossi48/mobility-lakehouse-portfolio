import duckdb

from mobility_lakehouse.config import WAREHOUSE_PATH


def main() -> None:
    with duckdb.connect(str(WAREHOUSE_PATH), read_only=True) as connection:
        print("Daily metrics")
        print(connection.sql("select * from gold_daily_metrics order by trip_date limit 10").df())
        print("\nTop pickup zones by revenue")
        print(connection.sql("select * from gold_zone_metrics order by total_revenue desc limit 10").df())


if __name__ == "__main__":
    main()

