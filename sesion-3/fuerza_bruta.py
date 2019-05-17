import string

password = input("Ingresa contraseña:\n")
attemps = 0

for i in range(len(password)):
    for char in string.ascii_lowercase:
        attemps += 1
        if char == password[i]:
            break

print('{} intentos'.format(attemps))
