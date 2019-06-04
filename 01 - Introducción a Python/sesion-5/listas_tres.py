from velocidad import promedio
from listas_dos import CAMPOS_CON_NUMEROS
from listas_uno import autos

CAMPO_DE_NOMBRE = 0
SEGUNDO_CAMPO = 1
PROMEDIO_CAMPO = 0

promedios = list(map(lambda campo: promedio(
    [auto[campo] for auto in autos]), CAMPOS_CON_NUMEROS))

promedio = promedios[PROMEDIO_CAMPO]

autos_filtrados = list(
    filter(lambda auto: auto[SEGUNDO_CAMPO] > promedio, autos))

for auto in autos_filtrados:
    print(auto)
