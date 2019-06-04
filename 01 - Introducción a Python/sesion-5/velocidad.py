from functools import reduce


def promedio(velocidades):
    n = len(velocidades)
    if n == 0:
        return 0
    suma = reduce(lambda suma_parcial,
                  velocidad: suma_parcial + velocidad, velocidades)
    return suma / n
