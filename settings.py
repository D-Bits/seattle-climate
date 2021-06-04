from sqlalchemy import create_engine
from datetime import datetime
import os 


### Settings to be used across DAGs ###

# Get the API token from an environment variable 
api_key = os.getenv("API_KEY")
# Set latitude and longitude for Seattle
lat = 47.6062
lon = -122.3321

# Create SQL Alchemy engine for loading data
db_conn = os.getenv("DB_CONN")
db_engine = create_engine(db_conn)

default_args = {
    "owner": "airflow",
    "start_date": datetime(2021, 5, 18),
    "retries": 1
}

