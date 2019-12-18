import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from settings import CSV_CITIES
from apps.cities.models import City


def get_cities_from_csv():
    return pd.read_csv(CSV_CITIES, names=['ville_id', 'ville_departement', 'ville_slug', 'ville_nom', 'ville_nom_simple', 'ville_nom_reel', 'ville_nom_soundex', 'ville_nom_metaphone', 'ville_code_postal', 'ville_commune', 'ville_code_commune', 'ville_arrondissement', 'ville_canton', 'ville_amdi', 'ville_population_2010', 'ville_population_1999', 'ville_population_2012', 'ville_densite_2010', 'ville_surface', 'ville_longitude_deg', 'ville_latitude_deg', 'ville_longitude_grd', 'ville_latitude_grd', 'ville_longitude_dms', 'ville_latitude_dms', 'ville_zmin', 'ville_zmax'], header=None, low_memory=False)



def cities_sort_asc(city):
    return city.sort_values('ville_population_2012', ascending=False)


def limit_dataframe_records(city, array_size):
    return city.head(array_size)


def reduce_dataframe(cities):
    return DataFrame(cities, columns=['ville_nom', 'ville_population_2012','ville_code_commune', 'ville_longitude_deg', 'ville_latitude_deg'])


def rename_dataframe_columns_cities(cities):
    return cities.rename(columns={"ville_nom": "name", "ville_population_2012": "population", "ville_code_commune": "code_insee", "ville_longitude_deg": "longitude", "ville_latitude_deg": "latitude"})


def prepare_data_from_csv():
    cities = get_cities_from_csv()
    return prepare_data(cities)


def prepare_data(cities):
    sorted = cities_sort_asc(cities)
    cities_50 = limit_dataframe_records(sorted, 50)
    cities_50_reduced = reduce_dataframe(cities_50)
    return cities_50_reduced


def prepare_graph(cities, graph_size):
    return cities.head(graph_size).plot(x='ville_nom', y='ville_population_2012', kind='barh')


def show_graph(cities, graph_size):
    prepare_graph(cities, graph_size)
    plt.show()


def dataframe_to_dict(df):
    dict_df = df.to_dict('records')
    return dict_df


def store_datas_in_dbb(list_dict, model):
    return model.insert_many(list_dict).execute()
