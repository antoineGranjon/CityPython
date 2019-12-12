from settings import csv
from apps.cities.cities import show_graph, prepare_data_from_csv


if __name__ == '__main__':
    cities = prepare_data_from_csv(csv)
    show_graph(cities, 10)
