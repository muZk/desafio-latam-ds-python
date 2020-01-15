select count(*)
from artists
right join user_profile ON artists.user_mboxsha1 = user_profile.user_mboxsha1
where artists.user_mboxsha1 is null;