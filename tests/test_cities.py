from settings import csv, max_city
from apps.cities.cities import read_csv, city_sort_ascending, show_simplified, narrow_column


def test_read_csv():
    city = get_csv()
    assert city['ville_nom'].iloc[0] == "OZAN"


def test_sorted_csv():
    sorted = city_sort_ascending(get_csv())
    assert sorted['ville_nom'].iloc[0] == "PARIS"


def test_csv_length():
    max_city = 10
    city_simplified = show_simplified(get_csv(), max_city)
    assert len(city_simplified) == max_city


def test_column():
    narrowed = narrow_column(get_csv())
    assert list(narrowed.columns == ['ville_nom', 'ville_population_2012'])


def get_csv():
    return read_csv(csv)
