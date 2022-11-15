## Description
In this assignment, you will import data from an external dataset and create a DataFrame. You'll save the data to a Parquet file and follow the steps to train the module using with Apache Spark. You'll complete the project by deploying the model to the IBM Watson Machine Learning (WML) Service. IBM WML is a scalable, scale-to-zero cloud service that supports training and serving of machine learning and deep learning models, providing a HTTP(S) endpoint for seamless consumption from third-party applications.  Detailed instructions provide guidance throughout the project.

More information about tasks, please refer to this [notebook](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/final_project.ipynb)
### Objectives

-  Pull-in data from the HMP dataset
-  Create a Spark data frame from the raw data
-  Store this to parquet (in Cloud Object Store)
-  Read it again (from Cloud Object Store)
-  Deploy this model to Train a ML-Model on that data set
-  Watson Machine Learning

Tech: Spark, SparkML, IBM Watson Studio, IBM Watson Machine Learning, ML

## Tasks and Solutions
- Task 1: Import the component library. (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/1-import-library.png "1")
- Task 2: Explore component library transformations. (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/2-parquet-to-csv.PNG "2")
- Task 3: Convert .csv to Parquet. (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/3-converted-parquet.PNG "3")
- Task 4: Perform model training. (1 pt) \
Anwser: 0.2067649473616369
- Task 5: Complete the model training. (1 pt) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/5-pmml.jpg "5")
- Task 6: Deploy the model to Watson Machine Learning. (1 pt)  \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/6-deploy_wml_pmml.PNG "6")
- Task 7: Perform model inference. (2 pts)  \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/7-model-inference.PNG "7")
- Task 8: HyperParameter Tuning. (3 pts) \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/8-hyper-tuning.PNG "8")
- Task 9: Resample data splits. (3 pts)  \
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/9-resample-data-splits.PNG "9")
- Task 10: RandomForest Classification. (6 pts)\
In this task, the data is loaded from the data lake (IBM Cloud Object Storage) as parquet and converted to .csv to do the data cleansing. After the cleansed data is gone through the ML Pipeline with SparkML under the Random Forest model with tunning parameters numTrees = [10, 20], maxDepth = [5, 7], seed_list = [1, None]. \
Please refer to the [notebook](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/train-random-forest.ipynb) trained on Watson Studio for more information or you can view it as [html](https://github.com/xzZero/DataEng_IBM/blob/main/12%20-%20Data%20Engineering%20and%20Machine%20Learning%20using%20Spark/Week3/random-forest.html)
