create or replace table gold_daily_metrics as
select
    cast(pickup_ts as date) as trip_date,
    count(*) as trip_count,
    round(sum(total_amount), 2) as total_revenue,
    round(avg(total_amount), 2) as average_fare,
    round(avg(distance_km), 2) as average_distance_km,
    round(avg(duration_minutes), 2) as average_duration_minutes,
    round(avg(case when fare_amount = 0 then 0 else tip_amount / fare_amount end), 4) as average_tip_rate
from silver_trips
group by 1;

