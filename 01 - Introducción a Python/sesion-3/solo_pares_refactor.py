tope = int(
    input("Ingrese un número para ver los números pares hasta dicho número\n"))

for n in range(1, tope + 1):
    if n % 2 == 0:
        print(n)
