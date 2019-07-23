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


def is_binary(serie):
    """ Returns true when the given serie is binary.

    Parameters
    ----------
    serie : Series

    Returns
    -------
    Boolean
        True when serie is binary.
    """
    return len(serie.value_counts()) == 2


def is_nominal(serie):
    """ Returns true when the given serie is nominal.

    Parameters
    ----------
    serie : Series

    Returns
    -------
    Boolean
        True when serie is nominal
    """

    values_count = serie.dropna().unique().size
    return values_count > 2 and values_count < 10


def humanize(col_name):
    t1 = {
        'school': 'Escuela del estudiante.',
        'sex': 'Sexo del estudiante',
        'age': 'Edad',
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

    t2 = {
        'age': 'Edad',
        'workclass': 'Naturaleza de la organización que emplea al individuo',
        'education': 'Nivel educacional del individuo',
        'capital-gains': 'Ingresos generados por inversiones fuera del trabajo asalariado',
        'capital-losses': 'Pérdidas generadas por inversiones fuera del trabajo asalariado',
        'fnlwgt': 'Ponderador muestral',
        'marital-status': 'Estado civil del individuo',
        'occupation': 'Ocupación del individuo',
        'relationship': 'Relación respecto a su familia',
        'race': 'Raza del encuestado ',
        'sex': 'Sexo del encuestado.',
        'hours-per-week': 'Cantidad de horas trabajadas por semana.',
        'native-country': 'País de origen',
        'income': 'Ingresos superiores a 50k',
    }

    if col_name in t1:
        return t1[col_name]
    if col_name in t2:
        return t2[col_name]
    return col_name


def plot_columns_behaviour(df, kind='countplot'):
    cols = list(df.columns)
    n_cols = 3
    n_rows = np.ceil(len(cols) / n_cols)
    plt.figure(figsize=(n_cols * 5, 5 * n_rows))

    for n, col_name in enumerate(cols):
        plt.subplot(n_rows, n_cols, n + 1)

        col = df[col_name]

        if kind == 'countplot':
            sns.countplot(y=col)
            plt.title(humanize(col_name))
            plt.xlabel("")
        else:
            sns.distplot(col, rug=True)
            plt.title(humanize(col_name))
            plt.xlabel("")
            plt.axvline(col.mean(), color='tomato',
                        linestyle='--', label='mean')
            plt.axvline(col.median(), color='green',
                        linestyle='--', label='median')
            plt.legend()
        plt.tight_layout()


def run_hip_test(df, col_name, group_by):
    """Runs a hypothesis test between two subsets of the dataframe.

    Returns true when we can reject null hypothesis at 95% significance about the median
    of the two groups being equal. The groups are created using a binary column (group_by)

    Parameters
    ----------
    df : DataFrame
        DataFrame with data to plot
    col_name : str
        Name of the column you want to plot
    group_by : str
        Name of the binary column used to create plot sets

    Raises
    ------
    NotImplementedError
        Throws this error if the group_by column is not binary
    """

    values = df[group_by].unique()

    if values.size != 2:
        raise NotImplementedError(
            "Only columns with two possible values are supported")

    group_1 = df[df[group_by] == values[1]][col_name].dropna()
    group_0 = df[df[group_by] == values[0]][col_name].dropna()
    t, pval = stats.ttest_ind(group_1, group_0, equal_var=False)
    return abs(t) > 1.96 and pval < 0.05


def graph_hist(df, col_name, group_by):
    """Plots histogram a column grouped by a binary column

    Parameters
    ----------
    df : DataFrame
        DataFrame with data to plot
    col_name : str
        Name of the column you want to plot
    group_by : str
        Name of the binary column used to create plot sets

    Raises
    ------
    NotImplementedError
        Throws this error if the group_by column is not binary
    """
    values = df[group_by].unique()

    if values.size != 2:
        raise NotImplementedError(
            "Only columns with two possible values are supported")

    group_0 = df[df[group_by] == values[0]][col_name].dropna()
    group_1 = df[df[group_by] == values[1]][col_name].dropna()

    def draw(group, group_name, color):
        plt.hist(group, alpha=0.5, color=color, density=True,
                 label='{} {}'.format(group_by, group_name))
        plt.axvline(np.mean(group), color=color)

    draw(group_0, values[0], 'lightblue')
    draw(group_1, values[1], 'tomato')
    plt.title('{} | {}'.format(group_by, col_name))
    plt.legend(loc='best')
    plt.show()


def plot_main_correlations(df, figsize=(15, 5)):
    """Plots main correlations between columns of the given dataframe.

    Parameters
    ----------
    df : DataFrame
        DataFrame with numeric columns used to compute correlation matrix
    """
    plt.figure(figsize=(15, 5))
    M = df.corr()
    best_corr = M[((M > 0.4) & (M < 1) | (M < -0.4))
                  ].dropna(axis=0, how='all').dropna(axis=1, how='all')
    sns.heatmap(best_corr, annot=True)
