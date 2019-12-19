from pandas import DataFrame


def ascending_sort_datafram(df, column):
    return df.sort_values(column, ascending=False)


def limit_dataframe_records(city, array_size):
    return city.head(array_size)


def reduce_dataframe(df, columns):
    return DataFrame(df, columns=columns)


def rename_dataframe_columns(cities, columns):
    return cities.rename(columns=columns)


def dataframe_to_dict(df):
    dict_df = df.to_dict('records')
    return dict_df


def store_datas_in_dbb(list_dict, model):
    return model.insert_many(list_dict).execute()
