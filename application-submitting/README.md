# Application submitting lab

The goals of this labs are to:
- Submit a pyspark application using `spark-submit`
- Add custom application properties to the `spark-submit`
- Use a `.properties` files to store the properties

## Lab resources

- The `taxi_streaming_analysis.py` pyspark script read streaming data from a socket and output aggregated results in parquet format to a HDFS directory.

## Submitting the application

- Go to the `application-submitting` directory
- Use `spark-submit` to submit the application:
  ```
  spark-submit --master yarn \
  --deploy-mode cluster \
  ./taxi_streaming_analysis.py \
  gauthier_taxi_streaming \
  edge1.au.adaltas.cloud \
  HDFS_OUTPUT_DIRECTORY \
  -f PORT_NUMBER
  ```
- To stop the application using `yarn application`
  - Use the `-list` command to find your application:
    ```
    yarn application -list | grep USERNAME
    ```
  - Kill the application using the `-kill` command and the application ID:
    ```
    yarn application -kill APP_ID
    ```
- Before re-submitting the app, clear the output and the checkpoint directory:
  ```
  hdfs dfs -rm -r /APP_OUTPUT_DIR/*
  hdfs dfs -rm -r /user/gauthier/checkpoint/*
  ```

## TO DO

1. Modify the `spark_taxi_streaming.py` file with your code from lab 3
2. Submit the application using `spark-submit`
3. Observe the results using Zeppelin (see `ece-2019/spark/ref/lab4` notebook)
4. Add custom application properties to the `spark-submit`
5. Write those properties in a `.properties` file
6. (Bonus) Write a bash script to automate the app submitting + directories cleaning in HDFS
7. (Bonus) Write a bash script to automate the application killing
