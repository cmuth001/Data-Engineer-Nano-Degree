import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events_table"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs_table"
songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

staging_events_table_create= ("""CREATE TABLE IF NOT EXISTS staging_events(
                                artist VARCHAR(MAX),
                                auth VARCHAR(25),
                                firstName VARCHAR(MAX),
                                gender CHAR(1),
                                itemSession INTEGER,
                                lastName VARCHAR(MAX),
                                length FLOAT4,
                                level VARCHAR(5),
                                location VARCHAR(MAX),
                                method VARCHAR(4),
                                page VARCHAR(12),
                                registration FLOAT8,
                                sessionId INTEGER,
                                song VARCHAR(MAX),
                                status INTEGER,
                                ts VARCHAR(MAX),
                                userAgent VARCHAR(MAX),
                                userId INTEGER
                            )
""")

staging_songs_table_create = ("""CREATE  TABLE IF NOT EXISTS staging_songs(
                                num_songs INTEGER,
                                artistId VARCHAR(MAX),
                                artistLatitude FLOAT8,
                                artistLongitude FLOAT8,
                                artistLocation VARCHAR(MAX),
                                artistName VARCHAR(MAX),
                                songId VARCHAR(MAX),
                                title VARCHAR(MAX),
                                duration FLOAT4,
                                year INTEGER
                            )
""")

songplay_table_create = ("""
""")

user_table_create = ("""
""")

song_table_create = ("""
""")

artist_table_create = ("""
""")

time_table_create = ("""
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
