import psycopg2

connection = psycopg2.connect(database="crime_db",user="postgres",password="_____________",host="localhost",port="5432")

!pip install sqlalchemy psycopg2-binary

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:______________@localhost:5432/crime_db")


monthly_sql = """SELECT "Month",COUNT(*) as crime_count FROM crime_data GROUP BY "Month" ORDER BY "Month";"""
monthly_df = pd.read_sql(monthly_sql,engine)

monthly_df

top_lsoa_sql = """SELECT "LSOA name", COUNT(*) AS crime_count FROM crime_data GROUP BY "LSOA name" ORDER BY crime_count DESC LIMIT 10;"""
top_lsoa_df = pd.read_sql(top_lsoa_sql,engine)

top_lsoa_df

crime_type_sql = """SELECT "Crime type",COUNT(*) AS crime_count FROM crime_data GROUP BY "Crime type" ORDER BY crime_count DESC;"""
crime_type_df = pd.read_sql(crime_type_sql,engine)

crime_type_df

#Visualization 

plt.figure(figsize=(10,6))
plt.plot( monthly_df["Month"],monthly_df["crime_count"])
plt.title("Monthly Crime Trend")
plt.xlabel("Month")
plt.ylabel("Crime Count")
plt.xticks(rotation=45)
plt.show()