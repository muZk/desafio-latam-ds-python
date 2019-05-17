import math


def letra_i(n):
    center_index = math.floor(n / 2)
    container = ''

    for row in range(n):
        outer_chars = ' '

        if row == 0 or row == n - 1:
            outer_chars = '*'

        for col in range(n):
            if col == center_index:
                container += '*'
            else:
                container += outer_chars

        if row != n - 1:
            container += '\n'
    return container
