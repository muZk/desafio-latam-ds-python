import sys

numeros = []

for num in sys.argv[1:]:
    numeros.append(int(num))

maximo = numeros[0]

for num in numeros:
    if num > maximo:
        maximo = num

print(maximo)
