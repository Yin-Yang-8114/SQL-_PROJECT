
import os
from dotenv import load_dotenv
from peewee import MySQLDatabase
import pymysql
 
pymysql.install_as_MySQLdb()
 
load_dotenv()
 
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
 
if not all([db_name, db_user, db_host, db_port]):
    raise ValueError("Database configuration is missing")
 
db = MySQLDatabase(
    db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=int(db_port),
)