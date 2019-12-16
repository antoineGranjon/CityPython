from settings import CSV_CITIES
from apps.cities.cities import read_from_csv, ascending_sort, show_simplified, reduce_dataframe


def test_read_csv():
    city = get_csv()
    assert city['ville_nom'].iloc[0] == "OZAN"


def test_sorted_csv():
    sorted = ascending_sort(get_csv())
    assert sorted['ville_nom'].iloc[0] == "PARIS"


def test_csv_length():
    max_city = 10
    city_simplified = show_simplified(get_csv(), max_city)
    assert len(city_simplified) == max_city


def test_column():
    narrowed = reduce_dataframe(get_csv())
    assert list(narrowed.columns == ['ville_nom', 'ville_population_2012', 'ville_code_commune'])


def get_csv():
    return read_from_csv(CSV_CITIES)
