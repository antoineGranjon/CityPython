from settings import CSV_CITIES, CSV_SCHOOLS
from apps.cities.cities import prepare_data_from_csv
from apps.schools.merge import merge_cities_and_schools, show_merged_datas_graph
from database import db


if __name__ == '__main__':
    db.connect()
    cities = prepare_data_from_csv(CSV_CITIES)
    merged = merge_cities_and_schools(CSV_CITIES, CSV_SCHOOLS)
    print(merged)
    show_merged_datas_graph(merged)
