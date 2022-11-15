## Description
In this assignment, 3 RDBMS (PostgreSQL, IBM Db2 and MySQL) are used. I have to handle the data for a coffee shop below:

![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/3%20-%20Python%20Project%20for%20data%20engineer/Week%201/Extract.PNG "Coffee data")

The [tasks]() are follows: 
- Identify entities, attributes and create and ERD from the sample data
- Normalize tables to snowflake schemas
- Define keys and relationships
- Import the data to the database in PostgreSQL via GeneratedScript.sql
- Create views from the database in PostgreSQL
- Create a materialized view and export the data from the view into .csv for further import to MySQL database of a marketing consultant for a marketing campaign
- Import the staff location data to the Db2 database of an external payroll company
- Import the exported .csv to the MySQL database

## Answers for peer-reviewed assigment
1. Task 1: Submit the list of entities that you identified as part of Task 1. 
- staff
- sales_outlet
- sales_transaction
- customer
- product
2. Task 2: Submit the list of attributes that you identified as part of Task 2. \
Answer: \
- sales_transaction: transaction_id, transaction_time, sales_outlet_id, staff_id, customer_id, product_id, quantity, price

O​thers:

- staff: staff_id, first_name, last_name, position, start_date, location
- sales_outlet: sales_outlet_id, sales_outlet_type, address, city, telephone, postal_code, manager
- customer: customer_id, customer_name, customer_email, customer_since, customer_card_number, birthdate, gender
- product: product_id, product_category, product_type, product_name, description, price
3. Task 3A: Submit the screenshot that you took as part of Task 3 and saved as Task3A.png or Task3A.jpg \
Answer:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/3%20-%20Python%20Project%20for%20data%20engineer/Week%201/Transform.PNG "Transform")
4. The prompted notebook can be downloaded [here](https://github.com/xzZero/DataEng_IBM/blob/main/3%20-%20Python%20Project%20for%20data%20engineer/Week%201/Final_Assignment_1.ipynb) or view in [Watson Studio](https://eu-de.dataplatform.cloud.ibm.com/analytics/notebooks/v2/10d01610-be63-42d2-b9cc-848c7106e3ef/view?access_token=429ad6c7494d9edb10ee76ff9f6c2c38c387d3969d69960215c95a2090ab904e)