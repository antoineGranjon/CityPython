import pandas as pd

from apps.cities.models import City
from settings import CSV_CITIES
from project.functions import ascending_sort_datafram, limit_dataframe_records, reduce_dataframe, \
    rename_dataframe_columns, dataframe_to_dict, store_datas_in_ddb


def get_cities_from_csv():
    return pd.read_csv(CSV_CITIES, names=['ville_id', 'ville_departement', 'ville_slug', 'ville_nom', 'ville_nom_simple', 'ville_nom_reel', 'ville_nom_soundex', 'ville_nom_metaphone', 'ville_code_postal', 'ville_commune', 'ville_code_commune', 'ville_arrondissement', 'ville_canton', 'ville_amdi', 'ville_population_2010', 'ville_population_1999', 'ville_population_2012', 'ville_densite_2010', 'ville_surface', 'ville_longitude_deg', 'ville_latitude_deg', 'ville_longitude_grd', 'ville_latitude_grd', 'ville_longitude_dms', 'ville_latitude_dms', 'ville_zmin', 'ville_zmax'], header=None, low_memory=False)


def prepare_data_from_csv():
    """ Récupère le csv et le converti en dataframe """
    cities = get_cities_from_csv()
    return prepare_data(cities)


def prepare_data(cities):
    """
        Prépare le dataframe au format attendu par la base de donnée

        Tri le dataframe des villes selon la population
        Limite le dataframe à 50 entrées
        Réduit les colonnes du dataframe pour ne garder que celles dont on a besoin dans la base de donnée
        Retourne ensuite le dataframe
    """
    sorted_cities = ascending_sort_datafram(cities, 'ville_population_2012')
    cities_50 = limit_dataframe_records(sorted_cities, 50)
    cities_50_reduced = reduce_dataframe(cities_50, ['ville_nom', 'ville_population_2012','ville_code_commune', 'ville_longitude_deg', 'ville_latitude_deg'])
    return cities_50_reduced


def prepare_graph(cities, graph_size):
    return cities.head(graph_size).plot(x='ville_nom', y='ville_population_2012', kind='barh')


def parse_csv_cities_to_database():
    cities = prepare_data_from_csv()
    cities_dataframe_renamed = rename_dataframe_columns(cities, {"ville_nom": "name", "ville_population_2012": "population", "ville_code_commune": "code_insee", "ville_longitude_deg": "longitude", "ville_latitude_deg": "latitude"})
    dic_cities = dataframe_to_dict(cities_dataframe_renamed)
    store_datas_in_ddb(dic_cities, City)
    cities_ddb = City.select().dicts()
    return cities_ddb
