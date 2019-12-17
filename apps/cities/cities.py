import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from settings import GRAPH_SIZE, ARRAY_SIZE
from apps.cities.models import City


def read_from_csv(file_path):
    return pd.read_csv(file_path, names=['ville_id', 'ville_departement', 'ville_slug', 'ville_nom', 'ville_nom_simple',
                                         'ville_nom_reel', 'ville_nom_soundex', 'ville_nom_metaphone',
                                         'ville_code_postal', 'ville_commune', 'ville_code_commune',
                                         'ville_arrondissement', 'ville_canton', 'ville_amdi', 'ville_population_2010',
                                         'ville_population_1999', 'ville_population_2012', 'ville_densite_2010',
                                         'ville_surface', 'ville_longitude_de', 'ville_latitude_deg',
                                         'ville_longitude_grd', 'ville_latitude_grd', 'ville_longitude_dms',
                                         'ville_latitude_dms', 'ville_zmin', 'ville_zmax'], header=None,
                       low_memory=False)


def ascending_sort(city):
    return city.sort_values('ville_population_2012', ascending=False)


def show_simplified(city, array_size):
    return city.head(array_size)


def reduce_dataframe(city):
    return DataFrame(city, columns=['ville_nom', 'ville_population_2012', 'ville_code_commune'])


def prepare_graph(city, graph_size):
    return city.head(graph_size).plot(x='ville_nom', y='ville_population_2012', kind='barh')


def show_graph(cities, graph_size):
    prepare_graph(cities, graph_size)
    plt.show()


def prepare_data_from_csv(csv_path):
    cities = read_from_csv(csv_path)
    return prepare_data(cities)


def prepare_data(cities):
    sorted = ascending_sort(cities)
    city_simplified = show_simplified(sorted, 50)
    cities_50_reduced = reduce_dataframe(city_simplified)
    return cities_50_reduced


def add_cities_to_database():
    City.insert_many()
