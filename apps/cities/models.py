from peewee import *
from database import db


class City(Model):
    code_insee = CharField(primary_key=True)
    name = CharField()
    population = IntegerField()
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        database = db  # This model uses the "cities.db" database.


City.create_table()
