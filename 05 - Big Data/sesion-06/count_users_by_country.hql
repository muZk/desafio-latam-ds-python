select country, count(*) as user_count from user_profile group by country order by user_count DESC;
