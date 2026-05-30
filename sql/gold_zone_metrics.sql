create or replace table gold_zone_metrics as
select
    pickup_zone,
    count(*) as trip_count,
    round(sum(total_amount), 2) as total_revenue,
    round(avg(distance_km), 2) as average_distance_km,
    round(avg(duration_minutes), 2) as average_duration_minutes
from silver_trips
group by 1;

