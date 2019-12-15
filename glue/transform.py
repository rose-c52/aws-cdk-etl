import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

glueContext = GlueContext(SparkContext.getOrCreate())

# Data Catalog: database and table name
db_name = ""
tbl_name = ""

# S3 location for input
input_dir = "s3://rose-ab-nyc-data-csv/AB_NYC_2019.csv"

# S3 location for output
output_dir = "s3://rose-transformed-data"

# Read data into a DynamicFrame using the Data Catalog metadata
# bnb_dyf = glueContext.create_dynamic_frame.from_catalog(database = db_name, table_name = tbl_name)

# OR read from s3
bnb_df = glueContext.read.format(
   "com.databricks.spark.csv").option(
   "header", "true").option(
   "inferSchema", "true").load(
   input_dir)

# Remove erroneous records
bnb_cleaned = bnb_df.where("`host_id` is NOT NULL")

# Turn it back to a dynamic frame
tmp = DynamicFrame.fromDF(bnb_cleaned, glueContext, "tmp")

# Rename, cast, and nest with apply_mapping
bnb_mapped = tmp.apply_mapping([('id', 'bigint', 'id', 'bigint'), 
                             ('host_id', 'bigint', 'host_id', 'bigint'),
                             ('neighbourhood_group', 'string', 'neighbourhood_group', 'string'),
                             ('neighbourhood', 'string', 'neighbourhood', 'string'),
                             ('room_type', 'string', 'room_type', 'string'),
                             ('price', 'bigint', 'price', 'bigint'),
                             ('minimum_nights', 'bigint','min_nights', 'bigint'),
                             ('number_of_reviews', 'bigint', 'number_of_reviews', 'bigint'),
                             ('last_review', 'string', 'last_review', 'double'),
                             ('reviews_per_month', 'double', 'reviews_per_month', 'double')])

# Write it out in Parquet
glueContext.write_dynamic_frame.from_options(frame = bnb_mapped, connection_type = "s3", connection_options = {"path": output_dir}, format = "parquet")