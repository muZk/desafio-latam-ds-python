def letra_x(n):
    contenedor = ''
    for fila in range(n):
        for columna in range(n):
            if columna == fila or columna == n - fila - 1:
                contenedor += '*'
            else:
                contenedor += ' '
        if fila != n - 1:
            contenedor += '\n'
    return contenedor
