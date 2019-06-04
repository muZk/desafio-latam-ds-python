def depositar(saldo, cantidad):
    return saldo + cantidad


def girar(saldo, cantidad):
    if saldo >= cantidad:
        return saldo - cantidad
    return False


def mostrar_menu(saldo=0):
    while True:
        print('Bienvenido al portal del Banco Amigo. Escoja una opción:')
        print('\t1. Consultar saldo')
        print('\t2. Hacer depósito')
        print('\t3. Realizar giro')
        print('\t4. Salir')

        opcion = input('\n')

        while not(opcion in ['1', '2', '3', '4']):
            opcion = input("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.\n")

        if opcion == '1':
            print('\nSu saldo es de {}\n'.format(saldo))
        elif opcion == '2':
            cantidad = int(input("\n"))
            saldo = depositar(saldo, cantidad)
            print('\nSu nuevo saldo es de {}\n'.format(saldo))
        elif opcion == '3':
            if saldo == 0:
                print("\nNo puede realizar giros. Su saldo es 0\n")
            else:
                resultado = False
                while resultado is False:
                    cantidad = int(input("\n"))
                    resultado = girar(saldo, cantidad)
                    if resultado is False:
                        print(
                            "\nNo se puede girar esta cantidad. Su saldo es de {}\n".format(saldo))
                saldo = resultado
                print('\nSu nuevo saldo es de {}\n'.format(saldo))
        else:
            break


mostrar_menu()
