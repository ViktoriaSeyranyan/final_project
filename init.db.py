import psycopg2 
from psycopg2 import sql


host = "localhost"
port = "5432"
user = "vika"          
password = "vik04" 
db_name = "dekanat_db" 

conn = psycopg2.connect(dbname="postgres", user=user, password=password, host=host, port=port)
conn.autocommit=True
cursor = conn.cursor()


cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))


cursor.execute(sql.SQL("ALTER DATABASE {} OWNER TO {}").format(sql.Identifier(db_name), sql.Identifier(user)))


cursor.close()
conn.close()

print(f"Database {db_name} created successfully with owner {user}")
