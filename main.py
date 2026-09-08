from db import db
from models import User, Delivery

def initialize_database():
    db.connect(reuse_if_open=True)
    db.create_tables([User,Delivery])

def main():
    initialize_database()
    print("Database configured and tables created successfully.")

main()