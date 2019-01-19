"""
Decrease the memory usage of the values and labels in the csv files.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gc  # garbage collector
import psutil


def convert_obj_columns_to_cat(df, exclude_cols):
    """
    Convert the datatype of object columns to category columns.

    :param df: Dataframe of the data
    :type  df: pandas.core.frame.DataFrame
    :param exclude_cols: set of columns to exclude from conversion
    :type  exclude_cols: set
    :returns: dataframe
    :rtype:   pandas.core.frame.DataFrame
    """

    column_list = df.select_dtypes(include=['object']).columns
    column_list = [col for col in column_list if col not in exclude_cols]
    for col in column_list:
        print("converting", col.ljust(30),
              "size: ", round(df[col].memory_usage(deep=True)*1e-6, 2), end="\t")
        df[col] = df[col].astype("category")
        print("->\t", round(df[col].memory_usage(deep=True)*1e-6, 2))
    return df


def downcast_df_int_columns(df):
    """
    Change integer types to decrease memory usage.

    :param df: Dataframe of the data
    :type  df: pandas.core.frame.DataFrame
    :returns: dataframe
    :rtype:   pandas.core.frame.DataFrame
    """

    list_of_columns = list(df.select_dtypes(
        include=["int32", "int64"]).columns)

    if len(list_of_columns) >= 1:
        # finds max string length for better status printing
        max_string_length = max([len(col) for col in list_of_columns])
        print("\ndowncasting integers for:", list_of_columns, "\n")

        for col in list_of_columns:
            print("reduced memory usage for:  ", col.ljust(max_string_length+2)[:max_string_length+2],
                  "from", str(round(df[col].memory_usage(deep=True)*1e-6, 2)).rjust(8), "to", end=" ")
            df[col] = pd.to_numeric(df[col], downcast="integer")
            print(str(round(df[col].memory_usage(deep=True)*1e-6, 2)).rjust(8))
    else:
        print("no columns to downcast")

    gc.collect()

    return df


def compress_labels(df):
    """
    Decrease memory size of labels

    :param df: Dataframe of the data
    :type  df: pandas.core.frame.DataFrame
    :returns: dataframe
    :rtype:   pandas.core.frame.DataFrame
    """

    df['status_group'] = df['status_group'].astype("category")
    df['id'] = pd.to_numeric(df['id'], downcast="integer")
    return df


def compress_X(df, exclude_cols):
    """
    Decrease memory size of inputss

    :param df: Dataframe of the data
    :type  df: pandas.core.frame.DataFrame
    :param exclude_cols: of of columns to exclude from object to
                         category conversion
    :type  exclude_cols: set
    :returns: dataframe
    :rtype:   pandas.core.frame.DataFrame
    """

    memory = df.memory_usage(index=True).sum()*1e-6

    print("memory used before preprocess: ", memory)

    # convert and compress objects to categories
    df = convert_obj_columns_to_cat(df, exclude_cols)

    # compress integer values
    df = downcast_df_int_columns(df)

    print("\navailable RAM:", psutil.virtual_memory())
    gc.collect()
    print("available RAM:", psutil.virtual_memory())

    memory = df.memory_usage(index=True).sum()*1e-6
    print("\nmemory used after preprocess: ", memory)

    return df