from __future__ import annotations

import duckdb
import pandas as pd
import streamlit as st

from mobility_lakehouse.config import WAREHOUSE_PATH


st.set_page_config(page_title="Mobility Lakehouse", layout="wide")


@st.cache_data
def load_table(table_name: str) -> pd.DataFrame:
    with duckdb.connect(str(WAREHOUSE_PATH), read_only=True) as connection:
        return connection.sql(f"select * from {table_name}").df()


def require_warehouse() -> None:
    if not WAREHOUSE_PATH.exists():
        st.error("Warehouse not found. Run `make pipeline` first.")
        st.stop()


require_warehouse()

daily_metrics = load_table("gold_daily_metrics").sort_values("trip_date")
zone_metrics = load_table("gold_zone_metrics").sort_values("total_revenue", ascending=False)
silver_trips = load_table("silver_trips")

st.title("Mobility Lakehouse")
st.caption("Zero-cost data engineering portfolio project")

total_trips = int(daily_metrics["trip_count"].sum())
total_revenue = float(daily_metrics["total_revenue"].sum())
average_fare = float(silver_trips["total_amount"].mean())
average_distance = float(silver_trips["distance_km"].mean())

metric_columns = st.columns(4)
metric_columns[0].metric("Trips", f"{total_trips:,}")
metric_columns[1].metric("Revenue", f"${total_revenue:,.2f}")
metric_columns[2].metric("Avg fare", f"${average_fare:,.2f}")
metric_columns[3].metric("Avg distance", f"{average_distance:,.2f} km")

left, right = st.columns([2, 1])

with left:
    st.subheader("Daily revenue")
    st.line_chart(daily_metrics, x="trip_date", y="total_revenue")

with right:
    st.subheader("Trips by pickup zone")
    st.bar_chart(zone_metrics, x="pickup_zone", y="trip_count")

st.subheader("Zone performance")
st.dataframe(
    zone_metrics[
        [
            "pickup_zone",
            "trip_count",
            "total_revenue",
            "average_distance_km",
            "average_duration_minutes",
        ]
    ],
    width="stretch",
    hide_index=True,
)

st.subheader("Recent curated trips")
st.dataframe(
    silver_trips.sort_values("pickup_ts", ascending=False).head(25),
    width="stretch",
    hide_index=True,
)
