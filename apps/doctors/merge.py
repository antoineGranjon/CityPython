import matplotlib.pyplot as plt
from apps.cities.controller import prepare_data_from_csv
from apps.doctors.controller import prepare_data_from_csv_doctors


def merge_cities_and_doctors():
    cities = prepare_data_from_csv()
    doctors = prepare_data_from_csv_doctors()
    cities_and_doctors_merged = cities.merge(doctors, left_on='ville_code_commune', right_on='Code commune')
    cities_and_doctors_merged['Nombre habitant par medecin'] = cities_and_doctors_merged['ville_population_2012'] / cities_and_doctors_merged['Nombre de medecins']
    cities_and_doctors_merged_sorted = cities_and_doctors_merged.sort_values(by='Nombre habitant par medecin', ascending=False)
    return cities_and_doctors_merged_sorted


def show_graphe_merged_cities_and_doctors(merged_datas):
    merged_datas.head(50).plot(x='ville_nom', y='Nombre habitant par medecin', kind='barh')
    plt.show()
