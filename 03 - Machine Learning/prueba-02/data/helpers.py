
import numpy as np
import pandas as pd
import re
from pandas.api.types import is_numeric_dtype
import math
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D
import mappings
import preproc_nyc_sqf as tuskas

from sklearn.metrics import classification_report, f1_score, accuracy_score

parse_model_name = lambda x: re.sub("'>'", "",
                                    str(x.estimator.__class__).split('.')[-1])

def to_time_str(time):
    if time >= 0 and time <= 1200:
        return 'MORNING'
    elif time > 1200 and time < 1900:
        return 'AFTERNOON'
    return 'EVENING'

def plot_model_performance(model, param_n=20, error_metric=True):
    """TODO: Docstring for plot_classification_report.
    :y_true: TODO
    :y_hat: TODO
    :returns: TODO
    """
    # preserve best param combination
    best_params = str(model.best_params_)
    # convert params combination to string and preserve
    # gather train and test scores, and params names, convert to dataframe
    tmp_df = pd.DataFrame({'params':list(map(lambda x: str(x), model.cv_results_['params'])),
                           'train_score':model.cv_results_['mean_train_score'],
                           'test_score': model.cv_results_['mean_test_score']})
    # sort
    tmp_df = tmp_df.sort_values(by='test_score', ascending=False)
    
    if error_metric is True:
        penalizer = 1
    else:
        penalizer = 0
    
    # limit size 
    if tmp_df.shape[0] > param_n:
        tmp_df = tmp_df.head(param_n)
    
    tmp_df['signal_optim'] = np.where(tmp_df['params'] == best_params, 'tomato', 'slategrey')
    
    tmp_grid = GridSpec(2, 1, height_ratios=[1, 4])
    
    plt.subplot(tmp_grid[0])
    plt.hist(penalizer - tmp_df['train_score'],
             label='Training Scores',
             alpha=.5)
    plt.hist(penalizer - tmp_df['test_score'],
             label = 'Testing Scores',
             alpha=.5)
    plt.legend()
    
    sns.despine()
    plt.subplot(tmp_grid[1])
    plt.scatter(penalizer - tmp_df['test_score'], tmp_df['params'], color=tmp_df['signal_optim'], label='Testing Scores', marker='*')
    plt.scatter(penalizer - tmp_df['train_score'], tmp_df['params'], color=tmp_df['signal_optim'], label='Training Scores', marker='o')
    plt.grid(axis='y', linestyle='--', lw=.2)
    plt.legend()
    sns.despine()
    plt.suptitle('{}\nBest hyperparams: {}\n Test Error:{}'.format(parse_model_name(model),model.best_params_, (1 - model.best_score_.round(2))))
    
    
def plot_benchmark(models):
    """TODO: Docstring for plot_classification_report.
    :y_true: TODO
    :y_hat: TODO
    :returns: TODO
    """
    # placeholder
    tmp_xaxis = []
    
    for index, values in enumerate(models):
        # preserve scikit-learn model name
        tmp_xaxis.append(re.sub("'>","",str(values.estimator.__class__).split('.')[-1]))
        # Visualize each test iteration
        plt.plot(values.cv_results_['mean_test_score'],
                 [index + .90] * len(values.cv_results_['params']),
                 'o', color='lightblue', alpha=.2)
        # Visualize each train iteration
        plt.plot(values.cv_results_['mean_train_score'],
                 [index + 1.10] * len(values.cv_results_['params']),
                 'o', color='pink', alpha=.2)
        # Signal test mean values
        plt.scatter(np.mean(values.cv_results_['mean_test_score']),
                    [index + .90], marker='|', s=100,
                    color='dodgerblue',zorder=3, label='Test')
        # Signal train mean values
        plt.scatter(np.mean(values.cv_results_['mean_train_score']),
                    [index + 1.10], marker='|', s=100,
                    color='tomato',zorder=3, label='Train')
        # Signal best performance on test
        plt.scatter(values.best_score_,
                    [index + 1], color='purple',
                    zorder=10)
        
    plt.yticks(range(1,len(tmp_xaxis) + 1), tmp_xaxis)
    plt.grid(axis='y')
    plt.legend(handles=[Line2D([0], [0], color='dodgerblue', marker="|", label='Test'),
                        Line2D([0], [0], color='tomato', marker='|', label='Training')])
        
        
def plot_classification_report(y_true, y_hat):
    """TODO: Docstring for plot_classification_report.
    :y_true: TODO
    :y_hat: TODO
    :returns: TODO
    """
    # process string and store in a list
    report = classification_report(y_true, y_hat).split()
    # keep values
    report = [i for i in report if i not in ['precision', 'recall', 'f1-score', 'support', 'avg']]
    # transfer to a DataFrame
    report = pd.DataFrame(np.array(report).reshape(len(report) // 5, 5))
    # asign columns labels
    report.columns = ['idx', 'prec', 'rec', 'f1', 'n']
    # preserve class labels
    class_labels = report.iloc[:np.unique(y_true).shape[0]].pop('idx').apply(int)
    # separate values
    class_report = report.iloc[:np.unique(y_true).shape[0], 1:4]
    # convert from str to float
    class_report = class_report.applymap(float)
    # convert to float average report
    average_report = report.iloc[-1, 1: 4].apply(float)

    colors = ['dodgerblue', 'tomato', 'purple', 'orange']

    for i in class_labels:
        plt.plot(class_report['prec'][i], [1], marker='x', color=colors[i])
        plt.plot(class_report['rec'][i], [2], marker='x', color=colors[i])
        plt.plot(class_report['f1'][i], [3], marker='x',color=colors[i], label=f'Class: {i}')

    plt.scatter(average_report, [1, 2, 3], marker='o', color='forestgreen', label='Avg')
    plt.yticks([1.0, 2.0, 3.0], ['Precision', 'Recall', 'f1-Score'])


def column_diff(df_1, df_2):
    '''
    Evalua si hay diferencias entre dataframes

    Parameters
    ----------
    df_1: DataFrame
        Dataframe que contiene los datos a revisar.

    df_2: DataFrame
        Dataframe que contiene los datos a revisar.

    Returns
    -------
    Listado con las columnas distintas.
    '''
    return set(df_1.columns).difference(set(df_2.columns))


def compare_diff_type(df_1, df_2, verbose=False):
    '''


    Parameters
    ----------
    df_1: DataFrame
        Dataframe que contiene los datos a revisar.

    df_2: DataFrame
        Dataframe que contiene los datos a revisar.

    verbose: Bool
        Verbosidad de la respuesta
    Returns
    -------
    Listado de columnas de df_1 que no está en df_2.
    '''
    diff_types = [col for col in df_1 if df_1[col].dtype != df_2[col].dtype]
    if verbose:
        for col in diff_types:
            print('Differences in column:', col, df_1[col].dtype, df_2[col].dtype)
    return diff_types


def compare_categorical(df_1, df_2, verbose=False):
    '''
    Imprime las columnas categóricas

    Parameters
    ----------
    df_1: DataFrame
        Dataframe que contiene los datos a revisar.

    df_2: DataFrame
        Dataframe que contiene los datos a revisar.

    verbose: Bool
        Verbosidad de la respuesta
    Returns

    Returns
    -------
    Sin retorno.
    '''
    categorical_columns = ([col for col in df_1.columns if df_1[col].dtype == np.object])
    for col in categorical_columns:
        print('\n', col)
        print(df_1[col].unique())
        print(df_2[col].unique())


def check_unique(df_1, df_2):
    '''

    Retorna los valores únicos da los dataframes ingresados
    Parameters
    ----------
    df_1: DataFrame
        Dataframe que contiene los datos a revisar.

    df_2: DataFrame
        Dataframe que contiene los datos a revisar.

    Returns
    -------
    Listado con valores únicos.
    '''
    categorical_columns = ([col for col in df_1.columns if df_1[col].dtype == np.object])
    unique = []

    for col in categorical_columns:
        values_1 = df_1[col].unique()
        values_2 = df_2[col].unique()
        len_1 = len(values_1)
        len_2 = len(values_2)
        if len_1 == len_2 and len_1 == 1:
            unique.append(col)
    return unique


def check_unique_and_nan(df):
    '''
    Evalua sobre las columnas categóricas corresponden a variables binarias

    Parameters
    ----------
    df: DataFrame
        Dataframe que contiene los datos a revisar.

    Returns
    -------
    Listado con colummas que cumplen el requisito.
    '''
    categorical_columns = ([col for col in df.columns if df[col].dtype == np.object])
    unique = []
    for col in categorical_columns:
        counts = df[col].value_counts(dropna=False)
        if len(counts.index) == 2:
            unique.append(col)
    return unique


def check_numeric(df):
    '''
    Evalua si variables que son tipo object puedan ser numéricas

    Parameters
    ----------
    df: DataFrame
        Dataframe que contiene los datos a revisar.

    Returns
    -------
    Sin retorno.
    '''
    categorical_columns = ([col for col in df.columns if df[col].dtype == np.object])
    for col in categorical_columns:
        counts = df[col].str.isnumeric().value_counts(dropna=False)
        if True in counts.index:
            print(col)
            print(counts)
            print('Numeric:', list(counts.index))
            print('Values:', df[col].value_counts(), '\n')

def draw_percentage(ax):
    '''
    Dibuja soobre las barras del countplot los porcentajes.

    Parameters
    ----------
    ax: Listado con objetos de Ejes

    Returns
    -------
    Sin retorno.
    '''
    bars = ax.patches
    half = int(len(bars)/2)
    left_bars = bars[:half]
    right_bars = bars[half:]
    for left, right in zip(left_bars, right_bars):
        height_l = left.get_height()
        height_r = right.get_height()
        total = height_l + height_r
        ax.text(left.get_x() + left.get_width()/2., height_l + 40, '{0:.0%}'.format(height_l/total), ha="center")
        ax.text(right.get_x() + right.get_width()/2., height_r + 40, '{0:.0%}'.format(height_r/total), ha="center")
        ax.set_xticklabels(ax.get_xticklabels(), rotation = 10) if len(ax.get_xticklabels()) > 5 else ""


def draw(features, objetive, df, columns = 2, title = ""):
    '''
    Dibuja countplot para atributos categóricos y displot para atributos numéricos

    Parameters
    ----------
    features: Listad de columnas características
    objetive: Nombre de la columna objetivo
    df: DataFrame
        Dataframe que contiene los datos a revisar.
    columns = número de columnas por para el subplor
    Returns
    -------
    Sin retorno.
    '''
    plt.figure(figsize=(20,20))
    features_len = len(features)
    for i, feature in enumerate(features):
        plt.subplot(math.ceil(features_len / columns) ,columns, i + 1)
        if is_numeric_dtype(df[feature]):
            sns.distplot(df[df[objetive] == 'YES'][feature])
            sns.distplot(df[df[objetive] == 'NO'][feature])
        else:
            ax = sns.countplot(x=feature, hue=objetive, data=df)
            draw_percentage(ax)
    plt.tight_layout()
    plt.subtitle = title

def create_suitable_dataframe(df_2009, df_2010):
    # Eliminamos columnas que están solo en 1 dataset y no en el otro
    df_2009.drop(columns=column_diff(df_2010, df_2009), inplace=True);
    df_2010.drop(columns=column_diff(df_2009, df_2010), inplace=True);

    # Comparamos los tipos de las columnas
    columns_diff_type = compare_diff_type(df_2009, df_2010)

    # Para los diferentes, intentamos transformar a número (ya que en uno son numerico y en el otro object)
    for col in columns_diff_type:
        df_2009[col] = pd.to_numeric(df_2009[col], errors='coerce', downcast='float')
        df_2010[col] = pd.to_numeric(df_2010[col], errors='coerce', downcast='float')

    # El dataset del 2010 tiene un solo valor faltante en detailcm
    df_2010.dropna(subset=['detailcm'], inplace=True)

    mappings.humanize_columns(df_2009)
    mappings.humanize_columns(df_2010)

    # Los datos que no existen están representados como string vacío, así que podemos reemplazarlos
    df_2009.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df_2010.replace(r'^\s*$', np.nan, regex=True, inplace=True)

    # Existen columnas que son numéricas pero están como string:
    for col in ['xcoord', 'ycoord']:
        df_2009[col] = pd.to_numeric(df_2009[col])
        df_2010[col] = pd.to_numeric(df_2010[col])

    # Existen columnas en ambos datasets que tienen 1 solo valor:
    uniques = check_unique(df_2009, df_2010)
    print('Columnas únicas eliminadas:', uniques)

    df_2009.drop(columns=uniques, inplace=True)
    df_2010.drop(columns=uniques, inplace=True)
    return pd.concat([df_2009, df_2010])

def clean(df):
    total_rows = df.shape[0]
    to_drop = set()

    for col in df:
        na_count = df[col].isna().sum()
        if na_count == total_rows:
            to_drop.add(col)

    for col in df:
        value_counts = df[col].value_counts(dropna=False)
        if len(value_counts.index) == 1:
            to_drop.add(col)

    print('Columnas a eliminar:', list(to_drop))
    df.drop(columns=to_drop, inplace=True)

def preprocess(df):
    df_preprocess = df.copy(deep=True)

    # Edad
    age = df_preprocess.year - tuskas.return_time_string(df_preprocess['dob']).map(lambda date: date.year)
    valid_ages = np.logical_and(age > 18, age < 100)
    mean_age = np.round(age[valid_ages].mean())
    age = np.where(valid_ages, age, mean_age)
    df_preprocess['age'] = age
    
    # Fechas
    df_preprocess['month'] = tuskas.return_time_string(df_preprocess['datestop']).apply(lambda x: x.month)
    df_preprocess['month'] = df_preprocess['month'].astype(np.str)
    df_preprocess['day_time'] = df_preprocess.timestop.map(to_time_str)
    
    # Estatura
    meters = df_preprocess['ht_feet'].astype(str) + '.' + df_preprocess['ht_inch'].astype(str)
    meters = meters.apply(lambda x: float(x) * 0.3048)
    df_preprocess['meters'] = meters
    
    # premname y detailcm
    premname = df_preprocess['premname']
    premname_count = premname.value_counts()
    other = premname.isin(premname_count[premname_count < 100].index)
    df_preprocess['premname'] = np.where(other, 'OTHER', premname)

    detailcm = df_preprocess['detailcm']
    detailcm_count = detailcm.value_counts()
    other = detailcm.isin(detailcm_count[detailcm_count < 244].index)
    df_preprocess['detailcm'] = np.where(other, 'OTHER', detailcm)
    
    # pct
    df_preprocess['pct'] = df_preprocess['pct'].astype(np.str)
    
    # arstoffn y sumoffen
    
    columns_to_drop = [
        'repcmd',
        'revcmd',
        'ser_num',
        'linecm',
        'crimsusp',
        'arstoffn',
        'datestop',
        'timestop',
        'dob',
        'ht_feet',
        'ht_inch',
        'weight',
        'crossst',
        'stinter',
        'post',
    ]
    
    columns_to_drop = [col for col in columns_to_drop if col in df_preprocess.columns]

    return df_preprocess.drop(columns=columns_to_drop)