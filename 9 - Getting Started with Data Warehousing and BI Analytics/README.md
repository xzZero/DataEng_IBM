## Description
In this project, you will act as a data engineer hired by a solid waste management company. The company collects and recycles solid waste across major cities in the country of Brazil. The company operates hundreds of trucks of different types to collect and transport solid waste. The company would like to create a data warehouse so that it can create reports like

- total waste collected per year per city
- total waste collected per month per city
- total waste collected per quarter per city
- total waste collected per year per trucktype
- total waste collected per trucktype per city
- total waste collected per trucktype per station per city

More information about [tasks]()
### Objectives
- Design a Data Warehouse
- Load data into Data Warehouse
- Write aggregation queries
- Create MQTs
- Create a Dashboard

### Data
The Data Warehouse have to be designed to fit with the sample data below:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/dag_args.PNG "1.1")\
Note that the Data Warehouse should be in snowflake schema for write-efficient.

## Tasks and Solutions
- Task 1: Design the dimension table MyDimDate (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/dag_args.PNG "1.1")
- Task 2: Design the dimension table MyDimWaste (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/dag_definition.PNG "dag_definition")
- Task 3: Design the dimension table MyDimZone (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/unzip_data.PNG "unzip_data")
- Task 4: Design the fact table MyFactTrips (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/extract_data_from_csv.PNG "extract_data_from_csv")
- Task 5: Create the dimension table MyDimDate (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/extract_data_from_tsv.PNG "extract_data_from_tsv")
- Task 6: Create the dimension table MyDimWaste  (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/extract_data_from_fixed_width.PNG "extract_data_from_fixed_width")
- Task 7: Create the dimension table MyDimZone (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/consolidate_data.PNG "consolidate_data")
- Task 8: Create the fact table MyFactTrips (2 pts) \
For this task, we can use the SELECT function to query the size of the database from information_schema.tables or using the show table status\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/transform.PNG "transform")
- Task 9: Load data into the dimension table DimDate (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/task_pipeline.PNG "task_pipeline")
- Task 10: Load data into the dimension table DimTruck (1 pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/submit_dag.PNG "submit_dag")
- Task 11: Load data into the dimension table DimStation (1 pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/unpause_dag.PNG "unpause_dag")
- Task 12: Load data into the fact table FactTrips (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/monitor_dag.PNG "monitor_dag")
- Task 13: Create a grouping sets query (2 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/start_zookeeper.PNG "start_zookeeper")
- Task 14: Create a rollup query (2 pts ) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/start_kafka.PNG "start_kafka")
- Task 15: Create a cube query using the columns year, city, station, average waste collected (2 pts ) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/create_toll_topic.PNG "create_toll_topic")
- Task 16: Create an MQT named max_waste_per_station using the columns city, station, trucktype, max waste collected  (2 pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/download_simulator.PNG "download_simulator")
- Task 17: Create a pie chart in the dashboard (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/configure_simulator.PNG "configure_simulator")
- Task 18: Create a bar chart in the dashboard (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/simulator_output.PNG "simulator_output")
- Task 19: Create a line chart in the dashboard (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/streaming_reader_code.PNG "streaming_reader_code")
- Task 20: Create a pie chart in the dashboard (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/data_reader_output.PNG "data_reader_output")
