import pandas as pd
import numpy as np

dataf = pd.read_csv('athlete_events.csv')

'''
1) Crear 4 nuevos subsets de datos, donde cada uno contenga, respectivamente, a los atletas 
que ganaron Oro, Plata, Bronce y aquellos que no ganaron medallas
'''

df_gold = dataf[dataf['Medal'] == 'Gold']
df_silver = dataf[dataf['Medal'] == 'Silver']
df_bronze = dataf[dataf['Medal'] == 'Bronze']
df_none = dataf[dataf['Medal'] == 'NA']
subsets = [df_gold, df_silver, df_bronze, df_none]
subset_names = ['Subset Oro', 'Subset Plata', 'Subset Bronze', 'Subset NA']

'''
2) Generar una nueva columna de nombre 'Female' para cada una de los subsets creados. En
esta nueva columna, se debe asignar 1 a las filas correspondientes a una mujer, y 0 a las
correspondientes a un hombre.
'''

for subset in subsets:
    females = subset['Sex'] == 'F'
    values = np.where(females, np.ones(females.size), np.zeros(females.size))
    subset['Female'] = values

'''
3) Reportar los 10 primeros países con mayor cantidad de participantes para cada una de los
subsets creados.
'''

print('\nPrimeros 10 países con mayor cantidad de participantes')

for index, subset in enumerate(subsets):
    print('\n{}'.format(subset_names[index]))
    print(subset['NOC'].value_counts().head(10))


'''
4) Reportar la cantidad de mujeres y hombres en cada uno de los subsets.
'''

print('\nCantidad de mujeres y hombres en cada subset')

for index, subset in enumerate(subsets):
    print('\n' + subset_names[index])
    print(subset['Sex'].value_counts())

'''
5) Generar una función que permita reportar las medias entre hombres y mujeres de una
columna
'''


def report_mean(df, analize, gender='Female'):
    group_1 = df[df['Sex'] == gender[0]]
    group_2 = df[df['Sex'] != gender[0]]
    mean_1 = group_1[analize].mean()
    mean_2 = group_2[analize].mean()
    if gender == 'Female':
        gender_2 = 'Male'
    else:
        gender_2 = 'Female'
    print('{} {}: {}'.format(gender, analize, mean_1))
    print('{} {}: {}'.format(gender_2, analize, mean_2))


'''
6)
    1. Aplicar la función del ejercicio 5 en los cuatro subsets creados.
    2. Reportar las medias de 'Height' y 'Weight' .
'''

for index, subset in enumerate(subsets):
    print('\n{}'.format(subset_names[index]))
    report_mean(subset, 'Height')
    report_mean(subset, 'Weight')
