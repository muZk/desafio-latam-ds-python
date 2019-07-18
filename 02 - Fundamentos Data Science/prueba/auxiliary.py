import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def binarize(df, column):
    """Adds a binarized column to the given dataframe using the minority as the true value

    Parameters
    ----------
    df : DataFrame
        DataFrame you want to binarize
    column : str
        Name of the column you want to binarize

    Raises
    ------
    NotImplementedError
        Throws this error if the column is not binary

    Returns
    -------
    DataFrame
        a new DataFrame with the new binarized column
    """

    copy = df.copy()

    counts = df[column].value_counts()

    if counts.count() != 2:
        raise NotImplementedError(
            "Only columns with two possible values are supported")

    minority = counts.index[0]
    majority = counts.index[1]

    if counts[minority] > counts[majority]:
        old_majority = minority
        minority = majority
        majority = old_majority

    new_column = column + '_' + minority
    copy[new_column] = None
    copy.loc[df[column] == minority, new_column] = 1
    copy.loc[df[column] == majority, new_column] = 0

    return copy


def binarize_columns(df, columns):
    """Adds binarized columns to the given dataframe
    The given columns are removed from the new dataframe

    Parameters
    ----------
    df : DataFrame
        DataFrame you want to binarize
    columns : list(str)
        Name of the columns you want to binarize

    Returns
    -------
    DataFrame
        a new DataFrame with the new binarized columns
    """

    copy = df.copy()

    for col_name in columns:
        copy = binarize(copy, col_name)

    copy = copy.drop(columns=columns)

    return copy


def dummierize_columns(data, columns):
    """Convert categorical variable into dummy variables

    Parameters
    ----------
    df : DataFrame
        DataFrame you want to convert
    columns : list(str)
        Name of the columns you want to convert

    Returns
    -------
    DataFrame
        a new DataFrame with the new dummy variables
    """

    df = data.copy()
    new_columns = []

    for col_name, col in df[columns].iteritems():
        counts = col.value_counts()
        values = list(counts.index)

        for value in values:
            new_column = "{}_{}".format(col_name, value)
            df[new_column] = None
            df.loc[col == value, new_column] = 'yes'
            df.loc[col.isin(
                list(filter(lambda x: x != value, values))), new_column] = 'no'
            new_columns.append(new_column)

    for col_name in new_columns:
        df = binarize(df, col_name)

    return df.drop(columns=new_columns).drop(columns=columns)


def is_discrete(col):
    return not(col.dtype == np.int64 and len(col.value_counts()) > 5)


def describe_columns(df):
    """Prints information about each column of the given dataframe.

    It uses .describe() for numerical columns and .value_counts() for discrete columns.

    Parameters
    ----------
    df : DataFrame
        DataFrame to describe
    """

    for i in df:
        col = df[i]

        if is_discrete(col):
            print(col.value_counts(normalize=True), "\n")
        else:
            print(col.describe(), "\n")


def plot_columns_behaviour(df):
    for n, i in enumerate(df):
        plt.subplot(1, 2, n % 2 + 1)

        col = df[i]

        if is_discrete(col):
            sns.countplot(y=df[i])
            plt.title(i)
            plt.xlabel("")
        else:
            sns.distplot(df[i])
            plt.title(i)
            plt.xlabel("")

        plt.tight_layout()
        plt.show()
