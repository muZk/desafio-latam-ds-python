CREATE TABLE user_profile(
    user_mboxsha1 VARCHAR(100),
    gender VARCHAR(10),
    age VARCHAR(100),
    country VARCHAR(100),
    signup VARCHAR(100)
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

CREATE TABLE artists(
    user_mboxsha1 VARCHAR(100),
    musicbrainz_artist_id VARCHAR(10),
    artist_name VARCHAR(100),
    plays VARCHAR(100)
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|';
