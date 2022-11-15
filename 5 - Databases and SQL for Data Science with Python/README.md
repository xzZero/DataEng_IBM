## Description
In this assignment contains two tracks: [intermediate SQL](#intermediate-sql-(week-5)) and [advanced SQL](#advanced-SQL-(week-6)) (including ACID transaction and advanced SQL join)

## Intermediate SQL (Week 5)
This task involves 3 datasets for the city of Chicago obtained from the Chicago Data Portal:
- [Chicago Socioeconomic Indicators](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01)
- [Chicago Public Schools](https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01)
- [Chicago Crime Data](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01) 

The tasks are follows: 
- Load the .csv data to the database (I used SQLite database here to diverisify the RDBMS)
- Problem 1: Find the total number of crimes recorded in the CRIME table.

- Problem 2: List community areas with per capita income less than 11000.

- Problem 3: List all case numbers for crimes involving minors?

- Problem 4: List all kidnapping crimes involving a child?(children are not considered minors for the purposes of crime analysis)

- Problem 5: What kind of crimes were recorded at schools?

- Problem 6: List the average safety score for all types of schools.

- Problem 7: List 5 community areas with highest % of households below poverty line.

- Problem 8: Which community area(number) is most crime prone?

- Problem 9: Use a sub-query to find the name of the community area with highest hardship index.

- Problem 10: Use a sub-query to determine the Community Area Name with most number of crimes?

## Answers for peer-reviewed assigment
1. Task 1: Submit the list of entities that you identified as part of Task 1. \
Answer: 
- staff
- sales_outlet
- sales_transaction
- customer
- product
2. Task 2: Submit the list of attributes that you identified as part of Task 2. \
Answer:
- sales_transaction: transaction_id, transaction_time, sales_outlet_id, staff_id, customer_id, product_id, quantity, price

O​thers:

- staff: staff_id, first_name, last_name, position, start_date, location
- sales_outlet: sales_outlet_id, sales_outlet_type, address, city, telephone, postal_code, manager
- customer: customer_id, customer_name, customer_email, customer_since, customer_card_number, birthdate, gender
- product: product_id, product_category, product_type, product_name, description, price
3. Task 3A: Submit the screenshot that you took as part of Task 3 and saved as Task3A.png or Task3A.jpg \
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task3A.PNG "Task3A")
4. Task 3B: Submit the screenshot that you took as part of Task 3 and saved as Task3B.png or Task3B.jpg.\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task3B.PNG "Task3B")
5. Task 4A: Submit the screenshot that you took as part of Task 4 and saved as Task4A.png or Task4A.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task4A.PNG "Task4A")
6. Task 4B: Submit the screenshot that you took as part of Task 4 and saved as Task4B.png or Task4B.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task4B.PNG "Task4B")
7. Task 5A: Submit the screenshot that you took as part of Task 5 and saved as Task5A.png or Task5A.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task5A.PNG "Task5A")
8.  Task 5B: Submit the screenshot that you took as part of Task 5 and saved as Task5B.png or Task5B.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task5B.PNG "Task5B")
9. Task 6A: Submit the screenshot that you took as part of Task 6 and saved as Task6A.png or Task6A.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task6A.PNG "Task6A")
10. Task 6B: Submit the screenshot that you took as part of Task 6 and saved as Task6B.png or Task6B.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task6B.PNG "Task6B")
11. Task 7: Submit the screenshot that you took as part of Task 7 and saved as Task7.png or Task7.jpg. (4 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task7.PNG "Task7")
12. Task 8: Submit the screenshot that you took as part of Task 8 and saved as Task8.png or Task8.jpg. (4 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task8.PNG "Task8")
13. Task 9: Take Submit the screenshot that you took as part of Task 9 and saved as Task9.png or Task9.jpg. (4 pts)	\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task9.PNG "Task9")
14. Task 10: Submit the screenshot that you took as part of Task 10 and saved as Task10.png or Task10.jpg. (4 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task10.PNG "Task10")

## Advanced SQL (Week 6)
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/existing_data.png "Coffee data")

The [tasks](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Task.pdf) are follows: 
- Identify entities, attributes and create and ERD from the sample data
- Normalize tables to snowflake schemas
- Define keys and relationships
- Import the data to the database in PostgreSQL via GeneratedScript.sql
- Create views from the database in PostgreSQL
- Create a materialized view and export the data from the view into .csv for further import to MySQL database of a marketing consultant for a marketing campaign
- Import the staff location data to the Db2 database of an external payroll company
- Import the exported .csv to the MySQL database

## Answers for peer-reviewed assigment
1. Task 1: Submit the list of entities that you identified as part of Task 1. \
Answer: 
- staff
- sales_outlet
- sales_transaction
- customer
- product
2. Task 2: Submit the list of attributes that you identified as part of Task 2. \
Answer:
- sales_transaction: transaction_id, transaction_time, sales_outlet_id, staff_id, customer_id, product_id, quantity, price

O​thers:

- staff: staff_id, first_name, last_name, position, start_date, location
- sales_outlet: sales_outlet_id, sales_outlet_type, address, city, telephone, postal_code, manager
- customer: customer_id, customer_name, customer_email, customer_since, customer_card_number, birthdate, gender
- product: product_id, product_category, product_type, product_name, description, price
3. Task 3A: Submit the screenshot that you took as part of Task 3 and saved as Task3A.png or Task3A.jpg \
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task3A.PNG "Task3A")
4. Task 3B: Submit the screenshot that you took as part of Task 3 and saved as Task3B.png or Task3B.jpg.\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task3B.PNG "Task3B")
5. Task 4A: Submit the screenshot that you took as part of Task 4 and saved as Task4A.png or Task4A.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task4A.PNG "Task4A")
6. Task 4B: Submit the screenshot that you took as part of Task 4 and saved as Task4B.png or Task4B.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task4B.PNG "Task4B")
7. Task 5A: Submit the screenshot that you took as part of Task 5 and saved as Task5A.png or Task5A.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task5A.PNG "Task5A")
8.  Task 5B: Submit the screenshot that you took as part of Task 5 and saved as Task5B.png or Task5B.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task5B.PNG "Task5B")
9. Task 6A: Submit the screenshot that you took as part of Task 6 and saved as Task6A.png or Task6A.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task6A.PNG "Task6A")
10. Task 6B: Submit the screenshot that you took as part of Task 6 and saved as Task6B.png or Task6B.jpg. (2 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task6B.PNG "Task6B")
11. Task 7: Submit the screenshot that you took as part of Task 7 and saved as Task7.png or Task7.jpg. (4 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task7.PNG "Task7")
12. Task 8: Submit the screenshot that you took as part of Task 8 and saved as Task8.png or Task8.jpg. (4 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task8.PNG "Task8")
13. Task 9: Take Submit the screenshot that you took as part of Task 9 and saved as Task9.png or Task9.jpg. (4 pts)	\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task9.PNG "Task9")
14. Task 10: Submit the screenshot that you took as part of Task 10 and saved as Task10.png or Task10.jpg. (4 pts)\
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/4%20-%20Introduction%20to%20Relational%20Databases%20(RDBMS)/Week4/exam/Task10.PNG "Task10")