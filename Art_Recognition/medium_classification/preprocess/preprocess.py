"""
Preprocess the SQLlite file by:
    condensing
    removing unnnecesary columns
    extracting labels from scores
"""

import pandas as pd
import sqlite3

import gc  # garbage collector

import importlib
import reduce_memory as rm

connection = sqlite3.connect("../data/bam-crowd-only.sqlite")
c = connection.cursor()


#======================================================================
# Load URLs
#======================================================================


def get_urls():
    """
    Get the dataframe that contains the labels from the SQL file

    :returns: dataframe containing the urls
    :rtype:   pandas.core.frame.DataFrame 
    """

    modules = pd.read_sql(
    "select * from modules",
    connection
    )

    modules.drop(
        ['mature_content', 'license'], 
        axis=1, inplace=True
    )

    modules_compressed = rm.compress_X(modules, {'src'})

    modules_compressed.set_index('mid', inplace=True)

    return modules_compressed


#======================================================================
# Get categorical labels from scores
#======================================================================


def drop_cols(df, col_names, operation):
    """
    Perform an operation to the column if the first part 
    of the name begins with a certain name.
    Ex. The first part of content_bicycle is content
    
    :param df: dataframe 
    :type  df: pandas.core.frame.DataFrame
    :param col_names: string to match
    :type  col_names: str
    :returns: dataframe 
    :rtype:   pandas.core.frame.DataFrame
    """
    
    for col in df.columns:
        if col.split('_')[0] == col_names:
            if operation == "drop":
                df = df.drop([col], axis=1)
            else:
                raise ValueError("Not an avaliable action")
    
    return df


def create_labels(df):
    """
    Create the labels using the scores

    :param df: dataframe 
    :type  df: pandas.core.frame.DataFrame
    :returns: dataframe of the labels
    :rtype:   pandas.core.frame.DataFrame
    """

    emotion_df = pd.DataFrame()
    media_df = pd.DataFrame()

    for col in df.columns:
        if col.split('_')[0] == "emotion":
            emotion_df = pd.concat([emotion_df, df[col]], axis=1)
        if col.split('_')[0] == "media":
            media_df = pd.concat([media_df, df[col]], axis=1)

    emotion_df.rename(
        lambda x: x.split('_')[1],
        axis='columns',
        inplace=True
    )
    media_df.rename(
        lambda x: x.split('_')[1],
        axis='columns',
        inplace=True
    )

    emotion_labels = emotion_df.idxmax(axis=1)
    media_labels = media_df.idxmax(axis=1)

    result = pd.DataFrame({
        "emotion": emotion_labels,
        "medium": media_labels
    })

    result = rm.convert_obj_columns_to_cat(result, {})

    return result


def get_labels():
    scores = pd.read_sql(
    "select * from scores",
    connection,
    index_col="mid"
    )

    scores.sort_index(axis=1, inplace=True)

    scores = drop_cols(scores, "content", "drop")

    labels = create_labels(scores)

    return labels


#======================================================================
# Merge the Scores and Modules
#======================================================================   
    

mod_and_scores = pd.concat(
    [get_urls(), get_labels()], 
    axis=1,
    join='inner'
)


#======================================================================
# Merge modules and crowd source labels
#====================================================================== 


def get_crowd_source_labels():
    """
    Preprocess the crowd source labels

    :returns: dataframe with labels
    :rtype:   pandas.core.frame.DataFrame
    """

    crowd_labels = pd.read_sql(
    "select * from crowd_labels",
    connection,
    index_col="mid"
    )

    crowd_labels = rm.convert_obj_columns_to_cat(crowd_labels, {})
    crowd_labels.sort_index(inplace=True)

    return crowd_labels


mod_and_crowd_labels = pd.concat(
    [get_urls(), get_crowd_source_labels()], 
    axis=1,
    join='inner'
)


#======================================================================
# Download as pickle
#====================================================================== 


mod_and_scores.to_pickle('../data/processed_data_scores.pkl')
mod_and_crowd_labels.to_pickle('../data/processed_data_crowd.pkl')