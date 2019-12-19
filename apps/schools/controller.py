import pandas as pd
import numpy as np
from apps.schools.models import School
from settings import CSV_SCHOOLS, CODE_INSEE
from project.functions import reduce_dataframe, rename_dataframe_columns, dataframe_to_dict, store_datas_in_dbb


def get_schools_from_csv():
    return pd.read_csv(CSV_SCHOOLS, sep=';')


def group_schools_by_insee(schools):
    return schools.groupby('Code commune').mean()


def prepare_data_from_csv_schools():
    """ Récupère le csv et le converti en dataframe """
    schools = get_schools_from_csv()
    return prepare_data(schools)


def prepare_data(schools):
    """
        Changement des codes commune, réduction des colonnes, regroupement des lycées et calcul de la note globale

        Changement de tout les codes commune des arrondissements de Paris, Lyon et Marseille pour ne garder qu'un seul code commune par ville
        Réduit les colonnes du dataframe pour ne garder que celles dont on a besoin dans la base de donnée
        Regroupe les lycées ayant le même code commune
        Calcul de la note globale
        retourne ensuite le dataframe
    """
    for city in CODE_INSEE:
        schools['Code commune'] = np.where(schools['Code commune'].isin(city[1]), city[0], schools['Code commune'])
    reduced_schools = reduce_dataframe(schools, ['Code commune', 'Taux Brut de Réussite Total séries', 'Taux_Mention_brut_toutes_series', 'Note globale'])
    grouped_schools = group_schools_by_insee(reduced_schools)
    grouped_schools['Note globale'] = (grouped_schools['Taux_Mention_brut_toutes_series'] + grouped_schools['Taux Brut de Réussite Total séries']) / 2
    return grouped_schools


def parse_csv_schools_to_database(merged_dataframe):
    reduced_df_schools = reduce_dataframe(merged_dataframe, ['Code commune', 'Taux Brut de Réussite Total séries', 'Taux_Mention_brut_toutes_series', 'Note globale'])
    renamed_df_schools = rename_dataframe_columns(reduced_df_schools, {"Code commune": "city", "Taux Brut de Réussite Total séries": "taux_reussite", "Taux_Mention_brut_toutes_series": "taux_mention", "Note globale": "note_globale"})
    dic_schools = dataframe_to_dict(renamed_df_schools)
    store_datas_in_dbb(dic_schools, School)
    schools_dbb = School.select().dicts()
    return schools_dbb
