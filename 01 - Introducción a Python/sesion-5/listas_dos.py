from velocidad import promedio
from listas_uno import autos

CAMPOS_CON_NUMEROS = [1, 2, 4]

promedios = list(map(lambda campo: promedio(
    [auto[campo] for auto in autos]), CAMPOS_CON_NUMEROS))

for promedio in promedios:
    print('Promedio: {}'.format(promedio))
