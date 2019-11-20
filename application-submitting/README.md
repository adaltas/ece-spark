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
