import os
from dotenv import load_dotenv
from peewee import MySQLDatabase

load_dotenv()
db_name = os.getenv("NAME")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
db_host = os.getenv("HOST")
db_port = os.getenv("PORT")

if not all([db_name,db_user,db_host,db_port]):
    raise ValueError("Database configuration is missing")

db = MySQLDatabase(db_name,user=db_user,password=db_password,host=db_host,port=int(db_port))