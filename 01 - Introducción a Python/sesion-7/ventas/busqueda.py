import sys

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

valores = [int(valor) for valor in sys.argv[1:]]

for valor in valores:
    mes_encontrado = False

    for mes, venta in ventas.items():
        if venta == valor:
            mes_encontrado = True
            print(mes)

    if not mes_encontrado:
        print('no encontrado')
