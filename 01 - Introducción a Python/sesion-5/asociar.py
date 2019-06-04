from velocidad import promedio


def zip(lista_1, lista_2):
    resultado = []
    for i in range(len(lista_1)):
        resultado.append((lista_1[i], lista_2[i]))
    return resultado


velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
             11, 11, 12, 12, 12, 12, 13, 13,
             13, 13, 14, 14, 14, 14, 15, 15,
             15, 16, 16, 17, 17, 17, 18, 18,
             18, 18, 19, 19, 19, 20, 20, 20,
             20, 20, 22, 23, 24, 24, 24, 24, 25]

distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
             17, 28, 14, 20, 24, 28, 26, 34, 34,
             46, 26, 36, 60, 80, 20, 26, 54, 32,
             40, 32, 40, 50, 42, 56, 76, 84, 36,
             46, 68, 32, 48, 52, 56, 64, 66, 54,
             70, 92, 93, 120, 85]

observaciones = zip(velocidad, distancia)
promedio_velocidad = promedio(velocidad)
promedio_distancia = promedio(distancia)


def velocidad_sobre_promedio(observacion):
    return observacion[0] > promedio_velocidad


def distancia_sobre_promedio(observacion):
    return observacion[1] > promedio_distancia


def velocidad_bajo_promedio(observacion):
    return observacion[0] < promedio_velocidad


def distancia_bajo_promedio(observacion):
    return observacion[1] < promedio_distancia


filtros = [
    filter(velocidad_bajo_promedio, observaciones),
    filter(lambda o: velocidad_bajo_promedio(o)
           and distancia_sobre_promedio(o), observaciones),
    filter(velocidad_sobre_promedio, observaciones),
    filter(lambda o: velocidad_sobre_promedio(o)
           and distancia_bajo_promedio(o), observaciones)
]

resultados = [list(filtro) for filtro in filtros]

conteos = [len(resultado) for resultado in resultados]

for conteo in conteos:
    print(conteo)
