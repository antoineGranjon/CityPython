import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from settings import CODE_INSEE


def get_schools_from_csv(file_path):
    return pd.read_csv(file_path, sep=';')


def reduce_dataframe(schools):
    return DataFrame(schools, columns=['Code commune', 'Taux Brut de Réussite Total séries', 'Taux_Mention_brut_toutes_series', 'Note globale'])


def sort_schools_by_insee(schools):
    return schools.sort_values('Code commune', ascending=False)


def group_schools_by_insee(schools):
    return schools.groupby('Code commune').mean()


def select_50_schools(schools):
    return schools.head(50)


def prepare_data_from_csv_schools(csv_path):
    schools = get_schools_from_csv(csv_path)
    return prepare_data(schools)


def prepare_data(schools):
    for city in CODE_INSEE:
        schools['Code commune'] = np.where(schools['Code commune'].isin(city[1]), city[0], schools['Code commune'])
    reduced_schools = reduce_dataframe(schools)
    grouped_schools = group_schools_by_insee(reduced_schools)
    grouped_schools['Note globale'] = (grouped_schools['Taux_Mention_brut_toutes_series'] + grouped_schools['Taux Brut de Réussite Total séries']) / 2
    return grouped_schools
