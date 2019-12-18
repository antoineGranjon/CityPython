from apps.cities.cities import prepare_data_from_csv, rename_dataframe_columns_cities, dataframe_to_dict, store_datas_in_dbb
from apps.schools.schools import prepare_data_from_csv_schools, rename_dataframe_columns_schools, reduce_dataframe_schools
from apps.schools.merge import merge_cities_and_schools, show_graphe_merged_cities_and_schools
from apps.cities.models import City
from apps.schools.models import School
from database import db


if __name__ == '__main__':
    db.close()
    db.connect()
    cities = prepare_data_from_csv()
    cities_dataframe_renamed = rename_dataframe_columns_cities(cities)
    dic_cities = dataframe_to_dict(cities_dataframe_renamed)
    q = City.delete()
    q.execute()
    cities_stored = store_datas_in_dbb(dic_cities, City)
    cities_dbb = City.select().dicts()
    print(list(cities_dbb))
    merged_dataframe = merge_cities_and_schools()
    reduced_df_schools = reduce_dataframe_schools(merged_dataframe)
    renamed_df_schools = rename_dataframe_columns_schools(reduced_df_schools)
    dic_schools = dataframe_to_dict(renamed_df_schools)
    q = School.delete()
    q.execute()
    schools_stored = store_datas_in_dbb(dic_schools, School)
    schools_dbb = School.select().dicts()
    print(list(schools_dbb))
    show_graphe_merged_cities_and_schools(merged_dataframe)
    db.close()
