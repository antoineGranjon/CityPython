import matplotlib.pyplot as plt
from apps.cities.cities import prepare_data_from_csv
from apps.schools.schools import prepare_data_from_csv_schools


def merge_cities_and_schools():
    cities = prepare_data_from_csv()
    schools = prepare_data_from_csv_schools()
    cities_and_schools_merged = cities.merge(schools, left_on='ville_code_commune', right_on='Code commune')
    cities_and_schools_merged_sorted = cities_and_schools_merged.sort_values(by='Note globale', ascending=False)
    return cities_and_schools_merged_sorted


def show_graphe_merged_cities_and_schools(merged_datas):
    merged_datas.head(20).plot(x='ville_nom', y='Note globale', kind='barh')
    plt.show()
