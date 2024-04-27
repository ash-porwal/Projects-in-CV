import psycopg2
import pandas as pd

conn = psycopg2.connect(
        user="postgres",
        dbname="dvdrental",
        password="", # enter password
        host="localhost"
        )

"""
cur = conn.cursor()
cur.execute("Select * from actor")
rows= cur.fetchall() 

for row in rows:
    print(row)
"""

# I will avoid above, and simply use pandas to fetch and write into file
# using pandas we dont even need to define headers
query = "Select * from actor"

df = pd.read_sql(query, conn)

df.to_csv("actor_test.csv", index=False)
conn.close()
