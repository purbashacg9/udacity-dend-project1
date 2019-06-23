# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"
log_table_drop = "DROP TABLE IF EXISTS logdata"

# CREATE TABLES
user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
  );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY,
    title varchar,
    artist_id varchar,
    year int,
    duration int
  );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS  artists (
    artist_id varchar PRIMARY KEY,
    name varchar,
    location varchar,
    lattitude varchar,
    longitude varchar
  );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
    time_id SERIAL PRIMARY KEY,
    start_time bigint,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
  );
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
    songplay_id  SERIAL PRIMARY KEY,
    start_time bigint,
    user_id int,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id int,
    location varchar,
    user_agent varchar ,
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (song_id) REFERENCES songs (song_id),
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
  );
 """)

log_table_create = ("""
    CREATE TABLE IF NOT EXISTS logdata (
    log_id  SERIAL PRIMARY KEY,
    start_time bigint,
    user_id int,
    level varchar,
    song varchar,
    artist varchar,
    length numeric,
    session_id int,
    location varchar,
    user_agent varchar ,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
  );
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name,last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, lattitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS
song_select = ("""
    SELECT songs.song_id, artists.artist_id  FROM artists
    inner JOIN songs ON artists.artist_id = songs.artist_id
    WHERE  songs.title=%s AND
    artists.name=%s AND 
    duration=%s;
""")
    
log_table_insert = ("""
INSERT INTO logdata (start_time, user_id, level, song, artist, length, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
""")    
    
# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create, log_table_create ]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
