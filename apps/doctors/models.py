from peewee import *
from apps.cities.models import City
from database import db


class Doctor(Model):
    city = ForeignKeyField(City)
    doctor_number = IntegerField()
    doctors_number_by_citizen = FloatField()

    class Meta:
        database = db


Doctor.create_table()
