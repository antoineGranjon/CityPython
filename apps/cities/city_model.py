from peewee import *
from database import db


class City(Model):
    name = CharField()
    code_insee = CharField(primary_key=True)
    population = AutoField()
    latitude = FloatField()
    longitude = FloatField()

    class Meta:
        database = db
