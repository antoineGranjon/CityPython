import matplotlib.pyplot as plt
from apps.cities.cities import prepare_data_from_csv
from apps.schools.calcul_critere import prepare_data_from_csv_schools


def merge_cities_and_schools(csv_cities_path, csv_schools_path):
    cities = prepare_data_from_csv(csv_cities_path)
    schools = prepare_data_from_csv_schools(csv_schools_path)
    cities_and_schools_merged = cities.merge(schools, left_on='ville_code_commune', right_on='Code commune')
    cities_and_schools_merged_sorted = cities_and_schools_merged.sort_values(by='Note globale', ascending=False)
    return cities_and_schools_merged_sorted


def show_merged_datas_graph(merged_datas):
    merged_datas.head(15).plot(x='ville_nom', y='Note globale', kind='barh')
    plt.show()
