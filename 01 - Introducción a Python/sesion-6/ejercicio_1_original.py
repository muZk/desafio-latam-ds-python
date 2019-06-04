import pandas as pd

df = pd.read_csv('athlete_events.csv')

ejercicio_1 = df.shape

ejercicio_2 = df['Games'].unique().size

# 3) Reportar el porcentaje (número entre 0 y 1) de atletas que participaron tanto en los juegos
# olímpicos de Verano como en los de Invierno

summer_or_winter = df[df['Season'].isin(['Summer', 'Winter'])]
ejercicio_3 = summer_or_winter['Season'].value_counts(normalize=True)
# athletes = summer_or_winter.value_counts()


# 4) Informar dónde fue la primera celebración de un Juego Olímpico de Verano. El resultado debe
# guardarse en una variable llamada ejercicio_4 .

summer = df[df['Season'] == 'Summer']
year_df = summer['Year']
ejercicio_4 = summer[year_df == year_df.min()]['City'].unique()

# Informar en qué ciudad fue la primera celebración de un Juego Olímpico de Invierno

winter = df[df['Season'] == 'Winter']
year_df = winter['Year']
ejercicio_5 = winter[year_df == year_df.min()]['City'].unique()

# Reportar los 10 primeros países con mayor cantidad de registros
ejercicio_6 = df['NOC'].value_counts()[:10]

# 7) Reportar el porcentaje de medallas asignadas (oro, bronce, plata)
with_medals = df['Medal'].isin(['Bronze', 'Silver', 'Gold'])
medals = df[with_medals]['Medal']
ejercicio_7 = medals.value_counts(normalize=True)

# 8) Reportar cuáles fueron los países participantes en las primeras olimpiadas de verano
summer = df[df['Season'] == 'Summer']
year_df = summer['Year']
ejercicio_8 = summer[year_df == year_df.min()]['NOC'].unique()

print(ejercicio_1)
print(ejercicio_2)
print(ejercicio_3)
print(ejercicio_4)
print(ejercicio_5)
print(ejercicio_6)
print(ejercicio_7)
print(ejercicio_8)
