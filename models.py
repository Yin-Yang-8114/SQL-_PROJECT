from datetime import datetime
from peewee import (Model,AutoField,CharField,FloatField,DateTimeField,ForeignKeyField,Check)
from db import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = AutoField()
    username = CharField(unique=True)
    password_hash = CharField()
    created_at = DateTimeField(default=datetime.now)
    class Meta:
        table_name = "users"

class Delivery(BaseModel):
    id = AutoField()
    package_name = CharField()
    destination = CharField()
    weight = FloatField(constraints=[Check('weight > 0')])
    status = CharField(default="Waiting")
    owner = ForeignKeyField(User,backref="deliveries",column_name="owner_id")
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "deliveries"