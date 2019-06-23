## Project Summary
The goal of this project was to design and populate a database and create tables optimized for running analytical queries for song play analysis.

The input datasets were json files containing songs and artists information and log files containing events arising from Sparkify's customers playing songs in the Sparkify application.  


### Schema Design
To analyze song plays by Sparkify's customers, created a database with star schema design composed of the following tables
  - songplays : A Transactional fact table that records facts about a song play by a Sparkify customer.
  - songs - Dimension table capturing songs data
  - artists - Dimension table capturing artists data
  - time - Dimension table capturing time information related to song plays
  - users - Dimension table capturing data on Sparkify's users.
  - logdata - Created this table to query contents of the log files and for testing accuracy of ETL script. 

### ETL   
Source data or ETL were in the file system in json files. There were two types of files -
  - songs.json - These contained information about a single song. They are arranged in a folder structure    based on the song's tracking id.
  -  YYYY-MM-DD-events.json - These files contain the data for a song play event. Each record contains the timestamp of the event, the user who is playing the song, session id of the user, location of the user, type of user - paid/free,  song played by the user, artist for the song, length of the song etc. A valid song play event is the one with page=NextSong.

The ETL steps are divided into of two sub-steps -
  - populating the songs and artists table from the songs data
  - populating songplays, time and users table from the logs data

## Project Files
  - sql_queries.py : contains the sql queries for creating and dropping tables and insert queries for populating the tables and select queries for getting information from songs and artists table.

  - create_tables.py  - contains helper methods for calling the individual queries from sql_queries.py for creating and dropping   tables. This is useful for restting the state of the database.

  - etl.ipynb - Jupyter Notebook containing the ETL code for populating tables from a single song file and a single log file.

  - etl.py - contains complete code for ETL process.

  - test.ipynb - Jupyter  Notebook containing queries for testing the Sparkify database.

  - Song Plays.ipynb - Jupyter Notebook containing some queries for running analysis on song plays.

  - data folder - contains the songs and log files.

  ## Running the  scripts

  Before running etl.py, wipe out the tables in Sparkfy database and recreate the dimension and fact tables and the database. Use  python create_tables.py to do this.

  Next run python etl.py to process the log and song files and populate the  tables.

  Use queries in test.ipynb to test the contents of the tables.
