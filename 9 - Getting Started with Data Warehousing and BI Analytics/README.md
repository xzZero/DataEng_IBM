## Description
In this project, you will act as a data engineer hired by a solid waste management company. The company collects and recycles solid waste across major cities in the country of Brazil. The company operates hundreds of trucks of different types to collect and transport solid waste. The company would like to create a data warehouse so that it can create reports like

- total waste collected per year per city
- total waste collected per month per city
- total waste collected per quarter per city
- total waste collected per year per trucktype
- total waste collected per trucktype per city
- total waste collected per trucktype per station per city

More information about [tasks](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/Task.pdf)
### Objectives
- Design a Data Warehouse
- Load data into Data Warehouse
- Write aggregation queries
- Create MQTs
- Create a Dashboard

### Data
The Data Warehouse have to be designed to fit with the sample data below:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/solid-waste-trips-new.png "solid-waste-trips-new")\
Note that the Data Warehouse should be in snowflake schema for write-efficient.

## Tasks and Solutions
- Task 1: Design the dimension table MyDimDate (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/1.PNG "1")
- Task 2: Design the dimension table MyDimWaste (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/2.PNG "2")
- Task 3: Design the dimension table MyDimZone (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/3.PNG "3")
- Task 4: Design the fact table MyFactTrips (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/4.PNG "4")
- Task 5: Create the dimension table MyDimDate (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/5.PNG "5")
- Task 6: Create the dimension table MyDimWaste  (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/6.PNG "6")
- Task 7: Create the dimension table MyDimZone (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/7.PNG "7")
- Task 8: Create the fact table MyFactTrips (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/8.PNG "8")
- Task 9: Load data into the dimension table DimDate (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/9a.PNG "9a")\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/9b.PNG "9b")
- Task 10: Load data into the dimension table DimTruck (1 pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/10a.PNG "10a")\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/10b.PNG "10b")
- Task 11: Load data into the dimension table DimStation (1 pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/11a.PNG "11a")\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/11b.PNG "11b")
- Task 12: Load data into the fact table FactTrips (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/12a.PNG "12a")\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/12b.PNG "12b")
- Task 13: Create a grouping sets query (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/13.PNG "13")
- Task 14: Create a rollup query (2 pts ) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/14.PNG "14")
- Task 15: Create a cube query using the columns year, city, station, average waste collected (2 pts ) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/15.PNG "15")
- Task 16: Create an MQT named max_waste_per_station using the columns city, station, trucktype, max waste collected  (2 pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/16.PNG "16")
- Task 17: Create a pie chart in the dashboard (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/17.PNG "17")
- Task 18: Create a bar chart in the dashboard (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/18.PNG "18")
- Task 19: Create a line chart in the dashboard (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/19.PNG "19")
- Task 20: Create a pie chart in the dashboard (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/9%20-%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week4/20.PNG "20")
