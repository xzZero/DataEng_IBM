## Description
For this project, the ELT is performed with the support of Airflow and Kafka. Assume you are a data engineer at a data analytics consulting company. You have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with different IT setup that use different file formats.  
In [the first Hands-on lab](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/Part1.pdf) your job is to collect data available in different formats and, consolidate it into a single file. As a vehicle passes a toll plaza, the vehicle's data like vehicle_id,vehicle_type,toll_plaza_id and timestamp are streamed to Kafka. In [the second Hands-on lab](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/Part2.pdf) your job is to create a data pipe line that collects the streaming data and loads it into a database.

## Tasks and Solutions
- Task 1.1: Define DAG arguments (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/dag_args.PNG "1.1")
- Task 1.2: Define the DAG (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/dag_definition.PNG "dag_definition")
- Task 1.3: Create a task to download data (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/unzip_data.PNG "unzip_data")
- Task 1.4: Create a task to extract data from csv file (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/extract_data_from_csv.PNG "extract_data_from_csv")
- Task 1.5: Create a task to extract data from tsv file (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/extract_data_from_tsv.PNG "extract_data_from_tsv")
- Task 1.6: Create a task to extract data from fixed width file (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/extract_data_from_fixed_width.PNG "extract_data_from_fixed_width")
- Task 1.7: Create a task to consolidate data extracted from previous tasks (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/consolidate_data.PNG "consolidate_data")
- Task 1.8: Transform the data (2 pts)\
For this task, we can use the SELECT function to query the size of the database from information_schema.tables or using the show table status\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/transform.PNG "transform")
- Task 1.9: Define the task pipeline (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/task_pipeline.PNG "task_pipeline")
- Task 1.10: Submit the DAG (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/submit_dag.PNG "submit_dag")
- Task 1.11: Unpause the DAG (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/unpause_dag.PNG "unpause_dag")
- Task 1.12: Monitor the DAG (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/monitor_dag.PNG "monitor_dag")
- Task 2.1: Start Zookeeper (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/start_zookeeper.PNG "start_zookeeper")
- Task 2.2: Start Kafka server (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/start_kafka.PNG "start_kafka")
- Task 2.3: Create a topic named toll (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/create_toll_topic.PNG "create_toll_topic")
- Task 2.4: Download the Toll Traffic Simulator (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/download_simulator.PNG "download_simulator")
- Task 2.5: Configure the Toll Traffic Simulator (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/configure_simulator.PNG "configure_simulator")
- Task 2.6: Run the Toll Traffic Simulator (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/simulator_output.PNG "simulator_output")
- Task 2.7: Configure streaming_data_reader.py (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/streaming_reader_code.PNG "streaming_reader_code")
- Task 2.8: Run streaming_data_reader.py (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/data_reader_output.PNG "data_reader_output")
- Task 2.9: Health check of the streaming data pipeline (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/8%20-%20ETL%20and%20Data%20Pipelines%20with%20Shell%2C%20Airflow%20and%20Kafka/Week5/output_rows.PNG "output_rows")