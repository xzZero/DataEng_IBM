{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p style=\"text-align:center\">\n",
    "    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork26764238-2022-01-01\" target=\"_blank\">\n",
    "    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\"  />\n",
    "    </a>\n",
    "</p>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "t8wxIYjBu_7O"
   },
   "source": [
    "### Analyse search terms on the e-commerce web server\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### In this assignment you will download the search term data set for the e-commerce web server and run analytic queries on it.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "5Kysvz9Eu2RT"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pyspark\n",
      "  Downloading pyspark-3.3.1.tar.gz (281.4 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m281.4/281.4 MB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25hCollecting py4j==0.10.9.5\n",
      "  Downloading py4j-0.10.9.5-py2.py3-none-any.whl (199 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m199.7/199.7 kB\u001b[0m \u001b[31m23.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hBuilding wheels for collected packages: pyspark\n",
      "  Building wheel for pyspark (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for pyspark: filename=pyspark-3.3.1-py2.py3-none-any.whl size=281845499 sha256=bf43fc0cf65dd0aa36c0d3951b0a74c9ad69f557f22f5e3221a39e9b0a836b04\n",
      "  Stored in directory: /home/jupyterlab/.cache/pip/wheels/91/aa/66/700b503fd714b56462975ab7bf33485ec26677c3c990e67e9a\n",
      "Successfully built pyspark\n",
      "Installing collected packages: py4j, pyspark\n",
      "Successfully installed py4j-0.10.9.5 pyspark-3.3.1\n",
      "Collecting findspark\n",
      "  Downloading findspark-2.0.1-py2.py3-none-any.whl (4.4 kB)\n",
      "Installing collected packages: findspark\n",
      "Successfully installed findspark-2.0.1\n"
     ]
    }
   ],
   "source": [
    "# Install spark\n",
    "!pip install pyspark\n",
    "!pip install findspark"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import findspark\n",
    "findspark.init()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pyspark import SparkContext, SparkConf\n",
    "from pyspark.sql import SparkSession"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "567chxjmvAPE"
   },
   "outputs": [],
   "source": [
    "# Start session"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "22/11/08 04:44:14 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable\n",
      "Setting default log level to \"WARN\".\n",
      "To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).\n"
     ]
    }
   ],
   "source": [
    "# Creating a spark context class\n",
    "sc = SparkContext()\n",
    "\n",
    "# Creating a spark session\n",
    "spark = SparkSession \\\n",
    "    .builder \\\n",
    "    .appName(\"Saving and Loading a SparkML Model\").getOrCreate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import Spark libs\n",
    "from pyspark.ml.feature import VectorAssembler\n",
    "from pyspark.ml.regression import LinearRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2022-11-08 04:44:40--  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv\n",
      "Resolving cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)... 169.63.118.104\n",
      "Connecting to cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)|169.63.118.104|:443... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: 233457 (228K) [text/csv]\n",
      "Saving to: ‘searchterms.csv’\n",
      "\n",
      "searchterms.csv     100%[===================>] 227.99K  --.-KB/s    in 0.009s  \n",
      "\n",
      "2022-11-08 04:44:40 (25.4 MB/s) - ‘searchterms.csv’ saved [233457/233457]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Download The search term dataset from the below url\n",
    "!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "            <div>\n",
       "                <p><b>SparkSession - in-memory</b></p>\n",
       "                \n",
       "        <div>\n",
       "            <p><b>SparkContext</b></p>\n",
       "\n",
       "            <p><a href=\"http://jupyterlab-u1221a4554:4040\">Spark UI</a></p>\n",
       "\n",
       "            <dl>\n",
       "              <dt>Version</dt>\n",
       "                <dd><code>v2.4.3</code></dd>\n",
       "              <dt>Master</dt>\n",
       "                <dd><code>local[*]</code></dd>\n",
       "              <dt>AppName</dt>\n",
       "                <dd><code>pyspark-shell</code></dd>\n",
       "            </dl>\n",
       "        </div>\n",
       "        \n",
       "            </div>\n",
       "        "
      ],
      "text/plain": [
       "<pyspark.sql.session.SparkSession at 0x7f1f30391910>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "spark"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the csv into a spark dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = spark.read.csv(\"searchterms.csv\", header=True, inferSchema=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the number of rows and columns\n",
    "# Take a screenshot of the code and name it as shape.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rows: 10000, Columns: 4\n"
     ]
    }
   ],
   "source": [
    "row = df.count()\n",
    "col = len(df.columns)\n",
    "print('Rows: %d, Columns: %d' %(row, col))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- day: integer (nullable = true)\n",
      " |-- month: integer (nullable = true)\n",
      " |-- year: integer (nullable = true)\n",
      " |-- searchterm: string (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the top 5 rows\n",
    "# Take a screenshot of the code and name it as top5rows.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Row(day=12, month=11, year=2021, searchterm='mobile 6 inch'),\n",
       " Row(day=12, month=11, year=2021, searchterm='mobile latest'),\n",
       " Row(day=12, month=11, year=2021, searchterm='tablet wifi'),\n",
       " Row(day=12, month=11, year=2021, searchterm='laptop 14 inch'),\n",
       " Row(day=12, month=11, year=2021, searchterm='mobile 5g')]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find out the datatype of the column searchterm?\n",
    "# Take a screenshot of the code and name it as datatype.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('searchterm', 'string')"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# How many times was the term `gaming laptop` searched?\n",
    "# Take a screenshot of the code and name it as gaminglaptop.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.createOrReplaceTempView('df')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------+\n",
      "|search_times|\n",
      "+------------+\n",
      "|         499|\n",
      "+------------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "spark.sql(\"SELECT COUNT(*) as search_times FROM df WHERE searchterm = 'gaming laptop'\").show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the top 5 most frequently used search terms?\n",
    "# Take a screenshot of the code and name it as top5terms.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[Stage 30:================================================>     (178 + 8) / 200]"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+-------------+------------+\n",
      "|   searchterm|search_times|\n",
      "+-------------+------------+\n",
      "|mobile 6 inch|        2312|\n",
      "|    mobile 5g|        2301|\n",
      "|mobile latest|        1327|\n",
      "|       laptop|         935|\n",
      "|  tablet wifi|         896|\n",
      "+-------------+------------+\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "                                                                                \r"
     ]
    }
   ],
   "source": [
    "spark.sql(\"SELECT searchterm, COUNT(*) as search_times FROM df GROUP BY searchterm ORDER BY 2 DESC LIMIT 5\").show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2022-11-08 05:01:08--  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/model.tar.gz\n",
      "Resolving cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)... 169.63.118.104\n",
      "Connecting to cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)|169.63.118.104|:443... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: 1490 (1.5K) [application/x-tar]\n",
      "Saving to: ‘model.tar.gz’\n",
      "\n",
      "model.tar.gz        100%[===================>]   1.46K  --.-KB/s    in 0s      \n",
      "\n",
      "2022-11-08 05:01:08 (7.29 MB/s) - ‘model.tar.gz’ saved [1490/1490]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# The pretrained sales forecasting model is available at  the below url\n",
    "!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/model.tar.gz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sales_prediction.model/\n",
      "sales_prediction.model/metadata/\n",
      "sales_prediction.model/metadata/part-00000\n",
      "sales_prediction.model/metadata/.part-00000.crc\n",
      "sales_prediction.model/metadata/_SUCCESS\n",
      "sales_prediction.model/metadata/._SUCCESS.crc\n",
      "sales_prediction.model/data/\n",
      "sales_prediction.model/data/part-00000-1db9fe2f-4d93-4b1f-966b-3b09e72d664e-c000.snappy.parquet\n",
      "sales_prediction.model/data/_SUCCESS\n",
      "sales_prediction.model/data/.part-00000-1db9fe2f-4d93-4b1f-966b-3b09e72d664e-c000.snappy.parquet.crc\n",
      "sales_prediction.model/data/._SUCCESS.crc\n"
     ]
    }
   ],
   "source": [
    "!tar -xvf model.tar.gz -C /resources/labs/DB0321EN/model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the sales forecast model.\n",
    "# Take a screenshot of the code and name it as loadmodel.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "# You need LinearRegressionModel to load the model\n",
    "from pyspark.ml.regression import LinearRegressionModel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "                                                                                \r"
     ]
    }
   ],
   "source": [
    "model = LinearRegressionModel.load('model/sales_prediction.model')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Param(parent='LinearRegression_6d5736f3dbe7', name='aggregationDepth', doc='suggested depth for treeAggregate (>= 2)'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='elasticNetParam', doc='the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='epsilon', doc='The shape parameter to control the amount of robustness. Must be > 1.0.'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='featuresCol', doc='features column name'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='fitIntercept', doc='whether to fit an intercept term'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='labelCol', doc='label column name'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='loss', doc='The loss function to be optimized. Supported options: squaredError, huber. (Default squaredError)'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='maxIter', doc='maximum number of iterations (>= 0)'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='predictionCol', doc='prediction column name'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='regParam', doc='regularization parameter (>= 0)'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='solver', doc='The solver algorithm for optimization. Supported options: auto, normal, l-bfgs. (Default auto)'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='standardization', doc='whether to standardize the training features before fitting the model'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='tol', doc='the convergence tolerance for iterative algorithms (>= 0)'),\n",
       " Param(parent='LinearRegression_6d5736f3dbe7', name='weightCol', doc='weight column name. If this is not set or empty, we treat all instance weights as 1.0')]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.params"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Param(parent='LinearRegression_6d5736f3dbe7', name='featuresCol', doc='features column name')"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.featuresCol"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using the sales forecast model, predict the sales for the year of 2023.\n",
    "# Take a screenshot of the code and name it as forecast.jpg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "df1 = spark.read.parquet('model/sales_prediction.model/data/part-00000-1db9fe2f-4d93-4b1f-966b-3b09e72d664e-c000.snappy.parquet')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "root\n",
      " |-- intercept: double (nullable = true)\n",
      " |-- coefficients: vector (nullable = true)\n",
      " |-- scale: double (nullable = true)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "df1.printSchema()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rows: 1, Columns: 3\n"
     ]
    }
   ],
   "source": [
    "row = df1.count()\n",
    "col = len(df1.columns)\n",
    "print('Rows: %d, Columns: %d' %(row, col))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-13019.989140447298"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.head()[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict(year):\n",
    "    assembler = VectorAssembler(inputCols=[\"year\"],outputCol=\"features\")\n",
    "    data = [[year,0]]\n",
    "    columns = [\"year\", \"sales\"]\n",
    "    df_ = spark.createDataFrame(data, columns)\n",
    "    df__ = assembler.transform(df_).select('features','sales')\n",
    "    predictions = model.transform(df__)\n",
    "    predictions.select('prediction').show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+------------------+\n",
      "|        prediction|\n",
      "+------------------+\n",
      "|175.16564294006457|\n",
      "+------------------+\n",
      "\n"
     ]
    }
   ],
   "source": [
    "predict(2023)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "Spark-de-assessment-1.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
