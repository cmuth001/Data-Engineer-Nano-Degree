## Introduction

A startup company called Sparkify provides music streaming to the users through the application. The songs details and the user activity data from the application are currently available and stored in the format of JSON.

If Sparkify wants to analyze the user's daily activities and provide future song recommendations, that would be very tough to query for the analysis and future recommendations from the JSON files. As the data goes increasing every day from Bytes to GBs and even more difficult for processing and analyzing the data with the JSON files.

Instead of storing the generated data from the user into the JSON files, I would recommend a cloud database which is widely used for modeling techniques and it helps in the fast retrieval of data and store large amount of data. This can be made even more efficient with the approach of the STAR schema creating in Redshift Cluster.

The STAR schema consists of one fact table referencing any number of dimension tables which helps the Sparkify for solving simplified common business logic.

* What is the next song Sparkify user would like to listen based on his past behavior.
* which song user would be more interested in listening to that particular point of time.
And much more complex business logics can be easily solved using the STAR schema method.

Created a STAR schema, optimized for song play analysis.

**Fact Table**: songplays: attributes referencing to the dimension tables.
**Dimension Tables**: users, songs, artists and time table.
This database will help the internal departments of the Sparkify company to do different kinds of analysis to recommend a Sparkify user.

* Favorite songs of user based on the week day: By joining songplay and songs and user table based on level.
* Recent listened to songs: By joining songplays and user table can show recommendation on the app based on subscription level.
* Can help in recommending most popular songs of the day/week.
