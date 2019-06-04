from itertools import groupby

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

resultado = {}
for venta in ventas.values():
    if not venta in resultado:
        resultado[venta] = 0
    resultado[venta] += 1

'''
valores_ventas = list(ventas.values())
valores_ventas.sort()
resultado = {valor: len(list(group))
             for valor, group in groupby(valores_ventas)}
'''

print(resultado)
