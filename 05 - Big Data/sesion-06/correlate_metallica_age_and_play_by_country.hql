select country, corr(cast(replace(plays, '"', '') as int), cast(replace(age, '"', '') as int)) as correlation
from user_profile
left join artists ON concat('"', artists.user_mboxsha1, '"') = user_profile.user_mboxsha1
where artists.artist_name = "metallica"
group by country
order by correlation asc;
