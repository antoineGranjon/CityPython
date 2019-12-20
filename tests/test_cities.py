from settings import CSV_CITIES
from apps.cities.controller import get_cities_from_csv, limit_dataframe_records
from project.functions import ascending_sort_datafram, reduce_dataframe


def test_read_csv():
    city = get_csv()
    assert city['ville_nom'].iloc[0] == "OZAN"


def test_sorted_csv():
    sorted = ascending_sort_datafram(get_csv(), 'ville_population_2012')
    assert sorted['ville_nom'].iloc[0] == "PARIS"


def test_csv_length():
    max_city = 10
    city_simplified = limit_dataframe_records(get_csv(), max_city)
    assert len(city_simplified) == max_city


def test_reduce_dataframe():
    narrowed = reduce_dataframe(get_csv(), ['ville_nom', 'ville_population_2012','ville_code_commune', 'ville_longitude_deg', 'ville_latitude_deg'])
    assert list(narrowed.columns == ['ville_nom', 'ville_population_2012','ville_code_commune','ville_longitude_deg', 'ville_latitude_deg'])


def get_csv():
    return get_cities_from_csv()
