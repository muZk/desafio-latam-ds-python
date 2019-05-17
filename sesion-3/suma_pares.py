tope = int(
    input("Ingrese un número para ver la suma de los pares hasta dicho número\n"))

suma = 0

for n in range(tope + 1):
    if n % 2 == 0:
        suma += n

print(suma)
