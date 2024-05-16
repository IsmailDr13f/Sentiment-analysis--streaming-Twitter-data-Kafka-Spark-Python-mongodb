
|Project Created By :      |
|------DRIEF ISMAIL        |
|------AMZIL AMMAR         |
|------ARICHI FATIMAZZOHRA |



This document outlines the methodology for executing the "Sentiment Analysis: Tweets" project. The project structure consists of 8 folders and 7 files:

Folders:

1..ipynb_checkpoints: This directory stores checkpoints for three notebooks: `data_stream_prediction.ipynb`, `insert_2_mongodb.ipynb`, and `Pipeline_modelLR.ipynb`.

2._pycache_: Contains compiled Python files for the `Clean_Func` model.

3.checkpoints: Saves checkpoints for JSON files.

4.json_files: Stores JSON files containing metadata and predictions, identified by the `.json` extension (including CRC).

5.kafka_prod_cons: Contains Python code for both the producer and consumer, along with data in CSV format.

6.pipeline_v1: Contains the machine learning model and the necessary pipeline for data processing.

7.tweet_v2: Holds only the Logistic Regression model for data prediction.

8.Visualisation: Includes Python code for a web application created with Streamlit.

Files:

1.Clean_Func.py: Contains necessary functions for data processing.

2.data_streamer_prediction.ipynb: Jupyter notebook with code for predicting sentiment from received tweets.

3.insert_2mongodb.ipynb: Jupyter notebook with code for saving predictions to a MongoDB database.

4.Pipeline_modelLR.ipynb: Jupyter notebook with code for the pipeline to process and predict sentiments.

5.README.txt: Provides project information.

6.twitter_training.csv: CSV file containing training data.

7.twitter_validation.csv: CSV file containing validation data.

------------------------------------------------------------------------------------------------
Here are the requirements for our project:
0. OS used: WINDOWS 11
1. Docker Desktop: To manage and run Docker containers on your local machine.
2. Jupyter Notebook: For interactive computing in Python and other languages.
3. Apache Spark 3.5.1: For large-scale data processing.
4. Python 3.11: The programming language used for development.
5. Kafka and Zookeeper images: For building and running Apache Kafka clusters.
6. Java 8 or Java 11: Required by Kafka, Spark, and other components.
7. MongoDB: For storing and managing data.
8. Streamlit: For building interactive web applications.
9. Pandas: For data manipulation and analysis.
10. NLTK: For natural language processing tasks.
11. Regex: For text pattern matching.
12. NumPy: For numerical computing.
13. PySpark 3.5.1: The Python API for Apache Spark.
14. PyMongo: For interacting with MongoDB from Python.
15. JSON: For data interchange.

Here are the steps to run the project:

1. Open Docker Desktop and start the Kafka and Zookeeper containers (assuming the images already exist in Docker).
2. Run the consumer (`consumer.py`) and producer (`producer.py`) scripts and ensure that data is received without any issues.
3. Run the `data_streamer_prediction.ipynb` file. Wait until the last cell finishes running.
4. Open MongoDB Compass and connect to your database (assuming the database "tweet_db" and collections "tweet_col" and "checkpoint" already exist).
5. Open the `insert_2_mongodb.ipynb` file and execute the code. Check MongoDB Compass to ensure that the data is received.
6. Navigate to the "Visualisation" folder and run the `Dashboard.py` file using the following command: `streamlit run Dashboard.py`. The web app will open in your browser.

Dashboard with Streamlit:

https://github.com/IsmailDr13f/Sentiment-analysis--streaming-Twitter-data-Kafka-Spark-Python-mongodb/assets/128002689/86ea0714-164c-479f-a623-8c2ee1dfcbd7

_______________________________________________
|  NB: For more details, refer to the report. |

