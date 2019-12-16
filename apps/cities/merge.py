import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from apps.cities.cities import prepare_data_from_csv
from apps.cities.calcul_critere import prepare_data_from_csv_schools


def merge_cities_and_schools(csv_cities_path, csv_schools_path):
    cities = prepare_data_from_csv(csv_cities_path)
    schools = prepare_data_from_csv_schools(csv_schools_path)
    cities_and_schools_merged = cities.merge(schools, left_on='ville_code_commune', right_on='Code commune')
    cities_and_schools_merged.sort_values('Taux Brut de Réussite Total séries')
    return cities_and_schools_merged
