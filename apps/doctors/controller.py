import pandas as pd
import numpy as np
from settings import CSV_DOCTORS, CODE_INSEE
from project.functions import reduce_dataframe, rename_dataframe_columns, dataframe_to_dict, store_datas_in_ddb
from apps.doctors.models import Doctor


def get_doctors_from_csv():
    return pd.read_csv(CSV_DOCTORS, sep=',')


def group_doctors_by_insee(doctors):
    return doctors.groupby('Code commune').size().reset_index(name='Nombre de medecins')


def prepare_data_from_csv_doctors():
    """ Récupère le csv et le converti en dataframe """
    doctors = get_doctors_from_csv()
    return prepare_data(doctors)


def prepare_data(doctors):
    """
        Changement des codes commune, réduction des colonnes, regroupement des lycées et calcul de la note globale

        Changement de tout les codes commune des arrondissements de Paris, Lyon et Marseille pour ne garder qu'un seul code commune par ville
        Réduit les colonnes du dataframe pour ne garder que celles dont on a besoin dans la base de donnée
        Regroupe les medecins ayant le même code commune
        Calcul du nombre de medecin par code commune
        retourne ensuite le dataframe
    """
    renamed_doctor = doctors.rename(columns={"c_depcom": "Code commune"})
    for city in CODE_INSEE:
         renamed_doctor['Code commune'] = np.where(renamed_doctor['Code commune'].isin(city[1]), city[0], renamed_doctor['Code commune'])
    reduced_doctors = reduce_dataframe(renamed_doctor, ['Code commune', 'Nombre de medecins'])
    grouped_doctors = group_doctors_by_insee(reduced_doctors)
    return grouped_doctors


def parse_csv_doctors_to_database(merged_dataframe):
    reduced_df_doctors = reduce_dataframe(merged_dataframe, ['Code commune', 'Nombre de medecins', 'Nombre habitant par medecin'])
    renamed_df_doctors = rename_dataframe_columns(reduced_df_doctors, {"Code commune": "city", "Nombre de medecins": "doctor_number",
                                                                       "Nombre habitant par medecin": "doctors_number_by_citizen"})
    dic_doctors = dataframe_to_dict(renamed_df_doctors)
    store_datas_in_ddb(dic_doctors, Doctor)
    doctors_ddb = Doctor.select().dicts()
    return doctors_ddb
