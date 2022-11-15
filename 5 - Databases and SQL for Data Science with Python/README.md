## Description
In this assignment contains two tracks: [intermediate SQL](#intermediate-sql-(week-5)) and [advanced SQL](#advanced-SQL-(week-6)) (including ACID transaction and advanced SQL join)

## Intermediate SQL (Week 5)
This task involves 3 datasets for the city of Chicago obtained from the Chicago Data Portal:
- [Chicago Socioeconomic Indicators](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01)
- [Chicago Public Schools](https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01)
- [Chicago Crime Data](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01) 

The tasks are follows: 
- Load the .csv data to the database (I used SQLite database here to diverisify the RDBMS)
- Problem 1: Find the total number of crimes recorded in the CRIME table.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/1.PNG "Task 1")
- Problem 2: List community areas with per capita income less than 11000.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/2.PNG "Task 2")
- Problem 3: List all case numbers for crimes involving minors?\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/3.PNG "Task 3")
- Problem 4: List all kidnapping crimes involving a child?(children are not considered minors for the purposes of crime analysis)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/4.PNG "Task 4")
- Problem 5: What kind of crimes were recorded at schools?\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/5.PNG "Task 5")
- Problem 6: List the average safety score for all types of schools.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/6.PNG "Task 6")
- Problem 7: List 5 community areas with highest % of households below poverty line.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/7.PNG "Task 7")
- Problem 8: Which community area(number) is most crime prone?\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/8.PNG "Task 8")
- Problem 9: Use a sub-query to find the name of the community area with highest hardship index.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/9.PNG "Task 9")
- Problem 10: Use a sub-query to determine the Community Area Name with most number of crimes?\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%205/10.PNG "Task 10")
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
*Notes: This task is on the honor track*\
This task involves 3 datasets for the city of Chicago obtained from the Chicago Data Portal:
- [Chicago Socioeconomic Indicators](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01)
- [Chicago Public Schools](https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01)
- [Chicago Crime Data](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2022-01-01) 

The tasks are follows: 
- Load the .csv data to the database (I used PostgreSQL database here to diverisify the RDBMS)
- Exercise 1: Using joins
    - Question 1: Write and execute a SQL query to list the school names, community names and average attendance for communities with a hardship index of 98.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/1.1.PNG "Q1.1")
    - Question 2: Write and execute a SQL query to list all crimes that took place at a school. Include case number, crime type and community name.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/1.2.PNG "Q1.2")
- Exercise 2: Creating a View
    - Question 1: Write and execute a SQL statement that returns just the school name and leaders rating from the view.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/2.PNG "Q2")
- Exericise 3: Creating a Stored Procedure
    - Question 1: Write the structure of a query to create or replace a stored procedure called UPDATE_LEADERS_SCORE that takes a in_School_ID parameter as an integer and a in_Leader_Score parameter as an integer. Don't forget to use the #SET TERMINATOR statement to use the @ for the CREATE statement terminator.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/3.1.PNG "Q3.1")
    - Question 2: Inside your stored procedure, write a SQL statement to update the Leaders_Score field in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID to the value in the in_Leader_Score parameter.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/3.2.PNG "Q3.2")
    - Question 3: Inside your stored procedure, write a SQL IF statement to update the Leaders_Icon field in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID using the following information.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/procedure_question.PNG "procedure_question")\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/3.3.PNG "Q3.3")
    - Question 4: Run your code to create the stored procedure. \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/3.4.PNG "Q3.4")
- Exercise 4: Using Transactions\
    - Question 1: Update your stored procedure definition. Add a generic ELSE clause to the IF statement that rolls back the current work if the score did not fit any of the preceding categories.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/4.1.PNG "Q4.1")
    - Question 2: Update your stored procedure definition again. Add a statement to commit the current unit of work at the end of the procedure.\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/5%20-%20Databases%20and%20SQL%20for%20Data%20Science%20with%20Python/Week%206/4.2.PNG "Q4.2")