## Description
You are a data engineer at a Data Analytics Consulting Company. Your company prides itself in being able to efficiently handle data in any format on any database on any platform. Analysts in the offices need to work with data on different databases, and with data in different formats. While they are good at analyzing data, they count on you to be able to move data from external sources into various databases, move data from one type of database to another, and be able to run basic queries on various databases.

More information about [tasks](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/Task.pdf)
### Objectives

- Replicate a Cloudant database.
- Create indexes on a Cloudant database.
- Query data in a Cloudant database.
- Import data into a MongoDB database.
- Query data in a MongoDB database.
- Export data from MongoDB.
- Import data into a Cassandra database.
- Query data in a Cassandra database.

Tech: Cloudant, MongoDB, Cassandra

## Tasks and Solutions
- Task 1: Replicate a remote database into your Cloudant instance. (1 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/1-replication.PNG "1")
- Task 2: Create an index for key "director", on the database movies using the HTTP API. (1pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/2-index-director.PNG "2")
- Task 3: Write a query to find all movies directed by Richard Gage using the HTTP API. (1 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/9-mongo-query.PNG "3")
- Task 4: Create an index for key "title", on the database movies using the HTTP API. (1 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/4-index-title.PNG "4")
- Task 5: Write a query to list only the keys year and director for the movie `Top Dog` using the HTTP API. (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/5-query-title.PNG "5")
- Task 6: Export the data from movies database into a file named movies.json. (2 pts)  \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/6-couchexport.PNG "6")
- Task 7: Import movies.json into mongodb server into a database named entertainment and collection named movies. (1 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/7-mongoimport.PNG "7")
- Task 8: Write a mongodb query to find the year in which most number of movies were released. (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/8-mongo-query.PNG "8")
- Task 9: Write a mongodb query to find the count of movies released after the year 1999. (1 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/9-mongo-query.PNG "9")
- Task 10. Write a query to find out the average votes for movies released in 2007. (2 pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/10-mongo-query.PNG "10")
- Task 11 - Export the fields _id, title, year, rating and director from movies collection into a file named partial_data.csv. (2 pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/11-mongoexport.PNG "11")\
- Task 12 - Import partial_data.csv into cassandra server into a keyspace named entertainment and table named movies. (1 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/12-cassandra-import.png "12")
- Task 13 - Write a cql query to count the number of rows in the movies table. (1 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/13-cassandra-query.PNG "13")
- Task 14 - Create an index for the column rating in the movies table using cql. (1 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/14-cassandra-index.PNG "14")
- Task 15 - Write a cql query to count the number of in the movies that are rated 'G'. (1 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/10%20-%20Introduction%20to%20NoSQL%20Databases/Week5/15-cassandra-query.PNG "15")
