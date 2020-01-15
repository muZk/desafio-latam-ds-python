select country, count(*) as result 
from user_profile
where gender NOT IN ("f", "m") OR age IN ('"99999"', '"-1337"')
group by country
order by result desc;
