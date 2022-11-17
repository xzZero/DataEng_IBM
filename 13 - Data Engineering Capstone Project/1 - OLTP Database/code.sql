--Create a database
CREATE DATABASE sales;

--Create sales_data table
USE sales;
CREATE TABLE sales_data(
    product_id INT NOT NULL PRIMARY KEY,
    customer_id INT,
    price INT,
    quantity INT,
    timestamp DATATIME
);
--Import oltpdata.csv to sales_data (2605 queries)

--List the tables in the database sales
USE sales;
SHOW TABLES;

--Find the count of sales_data
SELECT COUNT(*) FROM sales_data;

--CREATE index
CREATE INDEX ts on sales_data(timestamp);

--List indexes
SHOW INDEX FROM sales.sales_data;
