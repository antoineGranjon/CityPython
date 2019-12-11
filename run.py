from settings import csv, max_city
from apps.cities.cities import read_csv, city_sort_ascending, show_simplified, show_graph, plt


if __name__ == '__main__':
    city = read_csv(csv)
    sorted = city_sort_ascending(city)
    city_simplified = show_simplified(sorted, max_city)
    print(city_simplified)
    city_graph = show_graph(city_simplified)

    plt.show()
