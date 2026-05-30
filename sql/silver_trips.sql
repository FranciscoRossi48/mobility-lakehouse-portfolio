create or replace table silver_trips as
select
    cast(trip_id as integer) as trip_id,
    cast(pickup_ts as timestamp) as pickup_ts,
    cast(dropoff_ts as timestamp) as dropoff_ts,
    pickup_zone,
    dropoff_zone,
    cast(passenger_count as integer) as passenger_count,
    cast(distance_km as double) as distance_km,
    cast(fare_amount as double) as fare_amount,
    cast(tip_amount as double) as tip_amount,
    cast(total_amount as double) as total_amount,
    date_diff('minute', cast(pickup_ts as timestamp), cast(dropoff_ts as timestamp)) as duration_minutes
from bronze_trips
where
    trip_id is not null
    and pickup_ts is not null
    and dropoff_ts is not null
    and distance_km > 0
    and fare_amount >= 0
    and total_amount >= 0;

