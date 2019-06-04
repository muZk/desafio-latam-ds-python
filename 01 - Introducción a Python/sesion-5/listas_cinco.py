from velocidad import promedio
from listas_uno import autos

SEGUNDO_CAMPO = 1

promedio_segundo_campo = promedio([auto[SEGUNDO_CAMPO] for auto in autos])

autos_filtrados = filter(
    lambda auto: auto[SEGUNDO_CAMPO] > promedio_segundo_campo, autos)

valores = list(map(lambda auto: auto[SEGUNDO_CAMPO], autos_filtrados))

print(valores)
