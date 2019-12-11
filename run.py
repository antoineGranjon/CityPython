from settings import *
from apps.cities.cities import *


if __name__ == '__main__':
    city = read_csv(csv)
    sorted = city_sort_ascending(city)
    city_simplified = show_simplified(sorted, max_city)
    print(city_simplified)
    city_graph = show_graph(city)

    plt.show()
