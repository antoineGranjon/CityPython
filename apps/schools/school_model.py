from peewee import *
from apps.cities.city_model import City
from database import db


class School(Model):
    city = ForeignKeyField(City)
    taux_reussite = FloatField()
    taux_mention = FloatField()
    note_global = FloatField()

    class Meta:
        database = db
