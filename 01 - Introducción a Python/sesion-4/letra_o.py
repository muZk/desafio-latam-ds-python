def letra_o(n):
    container = ''
    for row in range(n):
        outer_chars = '*'
        center_chars = ' '
        if row == 0 or row == n - 1:
            center_chars = '*'

        for col in range(n):
            if col == 0 or col == n - 1:
                container += outer_chars
            else:
                container += center_chars

        if row != n - 1:
            container += '\n'
    return container
