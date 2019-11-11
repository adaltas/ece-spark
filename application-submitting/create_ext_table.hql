CREATE EXTERNAL TABLE ece.gauthier_fares_count (
  event_window STRUCT<start_time:TIMESTAMP,end_time:TIMESTAMP>,
  ride_count BIGINT,
  mean_total_fare DOUBLE
)
STORED AS PARQUET
LOCATION 'hdfs:///user/gauthier/spark/output/lab4';
