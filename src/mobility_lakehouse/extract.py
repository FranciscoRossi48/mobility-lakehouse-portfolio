from __future__ import annotations

import random
from datetime import datetime, timedelta

import pandas as pd

from mobility_lakehouse.config import BRONZE_DIR


ZONES = [
    "Centro",
    "Norte",
    "Sur",
    "Este",
    "Oeste",
    "Aeropuerto",
    "Universidad",
    "Terminal",
]


def build_trips(row_count: int = 2_000, seed: int = 42) -> pd.DataFrame:
    random.seed(seed)
    start = datetime(2026, 1, 1, 6, 0, 0)
    rows = []

    for trip_id in range(1, row_count + 1):
        pickup_ts = start + timedelta(minutes=random.randint(0, 60 * 24 * 30))
        duration_minutes = random.randint(4, 75)
        distance_km = round(random.uniform(0.8, 28.0), 2)
        base_fare = 1.2 + distance_km * random.uniform(0.8, 1.8)
        tip_amount = round(base_fare * random.choice([0, 0.05, 0.1, 0.15, 0.2]), 2)
        fare_amount = round(base_fare, 2)

        rows.append(
            {
                "trip_id": trip_id,
                "pickup_ts": pickup_ts.isoformat(),
                "dropoff_ts": (pickup_ts + timedelta(minutes=duration_minutes)).isoformat(),
                "pickup_zone": random.choice(ZONES),
                "dropoff_zone": random.choice(ZONES),
                "passenger_count": random.randint(1, 4),
                "distance_km": distance_km,
                "fare_amount": fare_amount,
                "tip_amount": tip_amount,
                "total_amount": round(fare_amount + tip_amount, 2),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    BRONZE_DIR.mkdir(parents=True, exist_ok=True)
    trips = build_trips()
    output_path = BRONZE_DIR / "trips.csv"
    trips.to_csv(output_path, index=False)
    print(f"Wrote {len(trips):,} trips to {output_path}")


if __name__ == "__main__":
    main()

