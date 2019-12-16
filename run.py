from settings import CSV_CITIES, CSV_SCHOOLS
from apps.cities.cities import show_graph, prepare_data_from_csv
from apps.cities.merge import merge_cities_and_schools


if __name__ == '__main__':
    cities = prepare_data_from_csv(CSV_CITIES)
    merged = merge_cities_and_schools(CSV_CITIES, CSV_SCHOOLS)
    print(merged)
    # show_graph(cities, 10)
