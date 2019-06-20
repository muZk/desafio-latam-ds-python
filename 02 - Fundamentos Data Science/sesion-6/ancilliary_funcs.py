import matplotlib.pyplot as plt
import numpy as np


def describe_columns(dataframe):
    col_stats = {}

    for var in dataframe:
        if dataframe[var].dtypes is np.dtype('object'):
            col_stats[var] = dataframe[var].value_counts(dropna=True)
        else:
            col_stats[var] = dataframe[var].describe()

    return col_stats


def missing_observations(dataframe, var, print_list=False):
    total_count = len(dataframe[var])
    nas = dataframe[var].isna()
    na_count = len(dataframe[nas])
    if print_list:
        return dataframe[nas]
    return na_count, na_count / total_count


def graph_hist(df, dataframe, var, sample_mean=False, true_mean=False):
    plt.figure(figsize=(20, 5))
    plt.title("Histograma de {}".format(var))
    dataframe[var].plot(kind='hist', color='green', alpha=.5, bins=100)
    if sample_mean:
        plt.axvline(dataframe[var].mean(),
                    color='dodgerblue', linestyle='--', lw=3)
    if true_mean:
        plt.axvline(df[var].mean(), color='red', linestyle='--', lw=3)


def z_score(serie):
    return (serie - serie.mean()) / serie.std()


def gen_dotplot(df, dataframe, plot_var, plot_by, global_stat=False, statistic='mean'):
    plt.figure(figsize=(20, 5))
    title = "Dotplot de {} (para la estadística {})"
    plt.title(title.format(plot_var, statistic))
    if statistic == 'mean':
        group_by = dataframe.groupby(plot_by)[plot_var].mean()
        value = dataframe[plot_var].mean()
        global_value = df[plot_var].mean()
    elif statistic == 'median':
        group_by = dataframe.groupby(plot_by)[plot_var].median()
        value = dataframe[plot_var].median()
        global_value = df[plot_var].median()
    else:  # z-score
        copy = dataframe.copy()
        x = copy[plot_var]
        copy['z_score'] = z_score(x)
        copy.dropna(subset=['z_score'], inplace=True)
        value = z_score(copy[plot_var]).mean()
        group_by = copy.groupby(plot_by)['z_score'].mean()
        global_value = z_score(df[plot_var]).mean()
    values = group_by.values
    indexes = group_by.index
    plt.plot(values, indexes, 'o')
    plt.axvline(value, color='blue')
    if global_stat:
        plt.axvline(global_value, color='tomato', linestyle='--')


def function(df, plot_var, plot_by, global_stat, ):
    # promedio z-score para plot_by
    # linea vertical: media z-score toda la muestra
    pass
