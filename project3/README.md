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

## DWH configurations and SETUP

### step-0
  * Create a new IAM user in your AWS account.
  * Give it AdministratorAccess and Attach policies
  * Use access key and secret key to create clients for EC2, S3, IAM, and Redshift.

### Step-1
  * See doc [IAM Role](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#client)
  * Create an IAM Role that makes Redshift able to access S3 bucket (ReadOnly)
  
### Step-2 
  * See doc [Create Cluster](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.create_cluster)
  * Create a RedShift Cluster and get the DWH_ENDPOIN(Host address) and DWH_ROLE_ARN and fill the config file.
  
## ETL Pipeline

1. Created tables tables to store the data from S3 buckets. 
2. Loading the data from S3 buckets to staging tables in the Redshift Cluster.
3. Inserted data into fact and dimension tables from the staging tables. 

## Usage
**sql_queries.py**: Contains all SQL queries of the project and this file can be used in multiple files.

**create_tables.py**: Run this file only after writing queries in the **sql_queries.py** file.
  drop_tables: This function is used to drop the tables.
  create_tables: This function is used to create tables. 
  
**etl.py**: Check the table schemas in your redshift database, if you find database schema is created successfully you can run this file. 
  load_staging_tables: This function is used to load the data from S3 to Redshift staging tables.
  insert_tables: This functionis used to insert data into fact and dimemsion tables from staging tables.

## execute files in the below order each time before pipeline

1.create_tables.py
```python
$ python3 create_tables.py
```

2. etl.py
```python
$ python3 etl.py
```
