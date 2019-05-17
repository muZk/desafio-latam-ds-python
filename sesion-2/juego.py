import sys
import random

PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERA = 'tijera'
jugadas = [PIEDRA, PAPEL, TIJERA]

INVALID_ARGUMENT = 'Argumento inválido: Debe ser piedra, papel o tijera.'

if len(sys.argv) > 1:
    jugada_jugador = sys.argv[1]

    if jugada_jugador in jugadas:
        jugada_computador = jugadas[random.randint(1, 3) - 1]
        print('Computador juega ' + jugada_computador)

        if jugada_computador == jugada_jugador:
            print('Empataste')
        else:
            jugador_gana = (jugada_jugador == PIEDRA and jugada_computador == TIJERA) or (
                jugada_jugador == TIJERA and jugada_computador == PAPEL) or (jugada_jugador == PAPEL and jugada_computador == PIEDRA)

            if jugador_gana:
                print('Ganaste')
            else:
                print('Perdiste')
    else:
        print(INVALID_ARGUMENT)
else:
    print(INVALID_ARGUMENT)
