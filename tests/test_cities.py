from settings import *
from apps.cities.cities import read_csv

def test_read_csv():
    city = read_csv(csv)
    assert city['ville_nom'].iloc[0] == "OZAN"
