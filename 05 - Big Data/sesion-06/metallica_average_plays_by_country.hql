select country, avg(plays) as average
from user_profile
left join artists ON concat('"', artists.user_mboxsha1, '"') = user_profile.user_mboxsha1
where artists.artist_name = "metallica"
group by country
order by average desc;

select country, avg(plays) as average
from user_profile
left join artists ON concat('"', artists.user_mboxsha1, '"') = user_profile.user_mboxsha1
where artists.artist_name = "metallica"
group by country
order by average asc;
