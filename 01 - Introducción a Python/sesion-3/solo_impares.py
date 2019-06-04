tope = int(
    input("Ingrese un número para ver los números impares hasta dicho número\n"))

for n in range(tope + 1):
    if n % 2 == 1:
        print(n)
