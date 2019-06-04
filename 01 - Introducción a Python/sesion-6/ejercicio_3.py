import pandas as pd
import numpy as np

df = pd.read_csv('athlete_events.csv')

'''
1) Generar un nuevo subset a partir del DataFrame original, que almacene todas las
observaciones correspondientes a Chile
'''

chile_df = df[df['NOC'] == 'CHI']

print(chile_df)

'''
2) Utilizando el subset generado, reportar la cantidad de atletas chilenos registrados en cada
año, y en qué año hubo la participación más alta.
'''

print('Atletas chilenos registrados por año:')
by_year = chile_df['Year'].value_counts()

print(by_year.sort_index())

print('\nAño con mayor participación')
print(by_year[by_year == by_year.max()])

'''
3) Reportar los nombres de todos los ganadores de alguna medalla.
'''

winners = chile_df[chile_df['Medal'] != 'NA']

print('\nNombre de ganadores de alguna medalla:')
print(winners['Name'])

'''
4) Reportar en qué año Chile obtuvo más medallas.
'''

print('\nAño en que Chile obtuvo más medallas:')
winners_by_year = winners['Year'].value_counts()
print(winners_by_year[winners_by_year == winners_by_year.max()])
