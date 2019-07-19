import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


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


def is_numeric(col):
    return (col.dtype == np.int64 or col.dtype == np.float64) and len(col.value_counts()) > 5


def is_discrete(col):
    return not is_numeric(col)


def is_binary(col):
    return len(col.value_counts()) == 2


def is_nominal(col):
    return len(col.value_counts()) == 5


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


def humanize(col_name):
    t = {
        'school': 'Escuela del estudiante.',
        'sex': 'Sexo del estudiante',
        'age': 'Edad del estudiante',
        'address': 'Ubicación de la casa del estudiante',
        'famsize': 'Tamaño de la familia',
        'Pstatus': 'Estado cohabitacional de los padres',
        'Medu': 'Nivel educacional de la madre',
        'Fedu': 'Nivel educacional del padre',
        'Mjob': 'Ocupación de la madre',
        'Fjob': 'Ocupación del padre',
        'reason': 'Razón para escoger la escuela',
        'guardian': 'Apoderado del estudiante',
        'traveltime': 'Tiempo de viaje entre hogar y colegio',
        'studytime': 'Horas semanales dedicadas al estudio',
        'failures': 'Número de clases reprobadas',
        'schoolsup': 'Apoyo educacional del colegio',
        'famsup': 'Apoyo educacional familiar',
        'paid': 'Clases particulares pagadas',
        'activities': 'Actividades extracurriculares',
        'nursery': 'Asistió a guardería infantil',
        'higher': 'Desea proseguir estudios superiores',
        'internet': 'Acceso a internet desde el hogar',
        'romantic': 'Relación romántica',
        'famrel': 'Calidad de las relaciones familiares',
        'freetime': 'Tiempo libre fuera del colegio',
        'goout': 'Salidas con amigos',
        'Dalc': 'Consumo de alcohol en día de semana',
        'Walc': 'Consumo de alcohol en fines de semana',
        'health': 'Estado de salud actual',
        'absences': 'Cantidad de ausencias escolares',
        'G1': 'Notas durante el primer semestre',
        'G2': 'Notas durante el segundo semestre',
        'G3': 'Promedio final',
    }
    return t[col_name]


def plot_columns_behaviour(df, kind='countplot'):
    cols = list(df.columns)
    n_cols = 3
    n_rows = np.ceil(len(cols) / n_cols)
    plt.figure(figsize=(n_cols * 5, 5 * n_rows))

    for n, col_name in enumerate(cols):
        plt.subplot(n_rows, n_cols, n + 1)

        col = df[col_name]

        if kind == 'countplot':
            sns.countplot(y=df[col_name])
            plt.title(humanize(col_name))
            plt.xlabel("")
        else:
            sns.distplot(df[col_name], rug=True)
            plt.title(humanize(col_name))
            plt.xlabel("")
            plt.axvline(df[col_name].mean(), color='tomato',
                        linestyle='--', label='mean')
            plt.axvline(df[col_name].median(), color='green',
                        linestyle='--', label='median')
            plt.legend()
        plt.tight_layout()


def run_hip_test(df, variable, binary):
    values = df[binary].unique()
    group_1 = df[df[binary] == values[1]][variable].dropna()
    group_0 = df[df[binary] == values[0]][variable].dropna()
    t, pval = stats.ttest_ind(group_1, group_0)
    return abs(t) > 1.96 and pval < 0.05


def graph_hist(df, variable, binary):
    values = df[binary].unique()
    group_1 = df[df[binary] == values[1]][variable].dropna()
    group_0 = df[df[binary] == values[0]][variable].dropna()

    def draw(group, group_name, color):
        plt.hist(group, alpha=0.5, color=color, density=True,
                 label='{} {}'.format(binary, group_name))
        plt.axvline(np.mean(group), color=color)

    draw(group_1, values[1], 'tomato')
    draw(group_0, values[0], 'lightblue')
    plt.title('{} | {}'.format(binary, variable))
    plt.legend(loc='best')
    plt.show()
