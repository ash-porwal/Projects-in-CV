import psycopg2

host = "localhost"
dbname = "dvdrental"
user = "postgres"
password = ""

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()
cur.execute("SELECT * FROM actor LIMIT 0")
# Accessing metadata
print("CUR description: ", cur.description)
column_names = [desc[0] for desc in cur.description]

print("Column Names:", column_names)

cur.close()
conn.close()

