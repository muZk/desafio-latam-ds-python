filas = int(input("Ingresa el numero de filas\n"))

for i in range(1, filas + 1):
    acumulador = ''
    for j in range(i):
        acumulador += str(j + 1)
    print(acumulador)
