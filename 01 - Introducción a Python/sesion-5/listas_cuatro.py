from listas_uno import autos
from velocidad import promedio

CAMPO_DE_NOMBRE = 0
CAMPO_BOOLEAN = -2

autos_filtrados = list(
    map(lambda auto: auto[CAMPO_DE_NOMBRE], filter(lambda auto: auto[CAMPO_BOOLEAN], autos)))

for auto in autos_filtrados:
    print(auto)
