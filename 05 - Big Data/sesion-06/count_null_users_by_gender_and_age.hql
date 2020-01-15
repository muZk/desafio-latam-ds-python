select count(*) as result from user_profile where gender NOT IN ("f", "m") AND age IN ('"99999"', '"-1337"');
