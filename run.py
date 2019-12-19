from apps.schools.merge import merge_cities_and_schools, show_graphe_merged_cities_and_schools
from apps.cities.models import City
from apps.schools.models import School
from apps.cities.controller import parse_csv_cities_to_database
from apps.schools.controller import parse_csv_schools_to_database
from database import db
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        help="Choose an action to execute",
        nargs="?",
        choices=[
            "from_csv",
            "from_database"
        ],
    )
    args = parser.parse_args()

    if args.action == "from_csv":
        merged_dataframe = merge_cities_and_schools()
        show_graphe_merged_cities_and_schools(merged_dataframe)

    if args.action == "from_database":
        db.close()
        db.connect()
        q = City.delete()
        q.execute()
        q = School.delete()
        q.execute()

        parse_csv_cities_to_database()

        merged_dataframe = merge_cities_and_schools()

        parse_csv_schools_to_database(merged_dataframe)

        show_graphe_merged_cities_and_schools(merged_dataframe)
        db.close()
