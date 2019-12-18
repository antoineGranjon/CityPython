import pandas as pd
import numpy as np
from pandas import DataFrame
from settings import CSV_SCHOOLS, CODE_INSEE
import matplotlib.pyplot as plt


def get_schools_from_csv():
    return pd.read_csv(CSV_SCHOOLS, sep=';')


def reduce_dataframe_schools(schools):
    return DataFrame(schools, columns=['Code commune', 'Taux Brut de Réussite Total séries', 'Taux_Mention_brut_toutes_series', 'Note globale'])


def sort_schools_by_insee(schools):
    return schools.sort_values('Code commune', ascending=False)


def group_schools_by_insee(schools):
    return schools.groupby('Code commune').mean()


def select_50_schools(schools):
    return schools.head(50)


def prepare_data_from_csv_schools():
    schools = get_schools_from_csv()
    return prepare_data(schools)


def prepare_data(schools):
    for city in CODE_INSEE:
        schools['Code commune'] = np.where(schools['Code commune'].isin(city[1]), city[0], schools['Code commune'])
    reduced_schools = reduce_dataframe_schools(schools)
    grouped_schools = group_schools_by_insee(reduced_schools)
    grouped_schools['Note globale'] = (grouped_schools['Taux_Mention_brut_toutes_series'] + grouped_schools[
        'Taux Brut de Réussite Total séries']) / 2
    return grouped_schools


def dataframe_to_dict(schools):
    dict_schools = schools.to_dict('records')
    return dict_schools


def rename_dataframe_columns_schools(schools):
    return schools.rename(columns={"Code commune": "city", "Taux Brut de Réussite Total séries": "taux_reussite", "Taux_Mention_brut_toutes_series": "taux_mention", "Note globale": "note_globale"})
