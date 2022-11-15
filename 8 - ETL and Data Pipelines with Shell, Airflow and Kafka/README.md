## Description
For this project, the ELT is performed with the support of Airflow and Kafka. Assume you are a data engineer at a data analytics consulting company. You have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with different IT setup that use different file formats.  
In the first Hands-on lab your job is to collect data available in different formats and, consolidate it into a single file. As a vehicle passes a toll plaza, the vehicle's data like vehicle_id,vehicle_type,toll_plaza_id and timestamp are streamed to Kafka. In the second Hands-on lab your job is to create a data pipe line that collects the streaming data and loads it into a database.

## Tasks and Solutions
- Task 1.1: Define DAG arguments (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/1.1.PNG "1.1")
- Task 1.2: Define the DAG (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/1.2.PNG "1.2")
- Task 1.3: Create a task to download data (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/1.3.PNG "1.3")
- Task 1.4: Create a task to extract data from csv file (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/1.4.PNG "1.4")
- Task 1.5: Create a task to extract data from tsv file (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/1.5.PNG "1.5")
- Task 1.6: Create a task to extract data from fixed width file (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/1.6.PNG "1.6")
- Task 1.7: Create a task to consolidate data extracted from previous tasks (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/2.1.PNG "2.1")
- Task 1.8: Transform the data (2 pts)\
For this task, we can use the SELECT function to query the size of the database from information_schema.tables or using the show table status\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/2.2.PNG "2.2")\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/2.2_.PNG "2.2_")
- Task 1.9: Define the task pipeline (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/2.3.PNG "2.3")
- Task 1.10: Submit the DAG (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/2.4.PNG "2.4")
- Task 1.11: Unpause the DAG (1pt)\
Performance before indexing:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/2.5_noindex.PNG "2.5_noindex")\
Performance after indexing:\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/2.5_index.PNG "2.5_index")
- Task 1.12: Monitor the DAG (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/2.6.PNG "2.6")
- Task 2.1: Start Zookeeper (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/2.7.PNG "2.7")
- Task 2.2: Start Kafka server (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/3.1.PNG "3.1")
- Task 2.3: Create a topic named toll (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/3.2.PNG "3.2")
- Task 2.4: Download the Toll Traffic Simulator (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/3.3.PNG "3.3")
- Task 2.5: Configure the Toll Traffic Simulator (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/3.4.PNG "3.4")
- Task 2.6: Run the Toll Traffic Simulator (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/3.5.PNG "3.5")
- Task 2.7: Configure streaming_data_reader.py (2pts)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/3.5.PNG "3.5")
- Task 2.8: Run streaming_data_reader.py (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/3.5.PNG "3.5")
- Task 2.9: Health check of the streaming data pipeline (1pt)\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/7%20-%20Relational%20Database%20Administration%20(DBA)/Week4/3.5.PNG "3.5")