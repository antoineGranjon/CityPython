import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


def read_csv(file_path):
    return pd.read_csv(file_path, names=['ville_id', 'ville_departement', 'ville_slug', 'ville_nom', 'ville_nom_simple',
                                         'ville_nom_reel', 'ville_nom_soundex', 'ville_nom_metaphone',
                                         'ville_code_postal', 'ville_commune', 'ville_code_commune',
                                         'ville_arrondissement', 'ville_canton', 'ville_amdi', 'ville_population_2010',
                                         'ville_population_1999', 'ville_population_2012', 'ville_densite_2010',
                                         'ville_surface', 'ville_longitude_de', 'ville_latitude_deg',
                                         'ville_longitude_grd', 'ville_latitude_grd', 'ville_longitude_dms',
                                         'ville_latitude_dms', 'ville_zmin', 'ville_zmax'], header=None,
                       low_memory=False)


def city_sort_ascending(city):
    return city.sort_values('ville_population_2012', ascending=False)


def show_simplified(city, max_city):
    return city.head(max_city)


def show_graph(city):
    plotVilles = DataFrame(city, columns=['ville_nom', 'ville_population_2012'])
    return plotVilles.head(10).plot(x='ville_nom', y='ville_population_2012', kind='barh')
