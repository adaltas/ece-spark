import argparse

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, window

parser = argparse.ArgumentParser(
    description='Process NYC Taxi datasets in streaming using sockets')
parser.add_argument('appname', type=str, help='The Spark application name')
parser.add_argument('sockethostname', type=str,
                    help='The hostname on which to listen to the socket')
parser.add_argument('outputpath', type=str,
                    help='The HDFS path where to write the CSV output')
parser.add_argument('-f', '--faresport', type=int, default=11111,
                    help='The port on which the fares dataset is streamed')
parser.add_argument('-r', '--ridesport', type=int, default=11112,
                    help='The port on which the rides dataset is streamed')

args = parser.parse_args()

spark = SparkSession \
    .builder \
    .appName(args.appname) \
    .getOrCreate()

fares_raw = spark \
    .readStream \
    .format("socket") \
    .option("host", args.sockethostname) \
    .option("port", args.faresport) \
    .load()

# Parse the socket message "manually"
fares = fares_raw.select(
    split(fares_raw.value, ',')[0].alias('ride_id').cast('int'),
    split(fares_raw.value, ',')[1].alias('taxi_id').cast('int'),
    split(fares_raw.value, ',')[2].alias('driver_id').cast('int'),
    split(fares_raw.value, ',')[3].alias('start_time').cast('timestamp'),
    split(fares_raw.value, ',')[4].alias('payment_type'),
    split(fares_raw.value, ',')[5].alias('tip').cast('float'),
    split(fares_raw.value, ',')[6].alias('tolls').cast('float'),
    split(fares_raw.value, ',')[7].alias('total_fare').cast('float')
)

fares_count = fares \
    .withWatermark('start_time', '5 minutes') \
    .groupBy(window(fares.start_time, '2 minutes', '2 minutes')) \
    .agg({'ride_id': 'count', 'total_fare': 'mean'})

fares_count_query = fares_count \
    .writeStream \
    .outputMode('complete') \
    .format('csv') \
    .option('path', args.outputpath) \
    .start()
