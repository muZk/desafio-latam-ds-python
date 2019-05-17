import string


def gen(length):
    container = ''
    for i in range(length):
        container += string.ascii_lowercase[i % len(string.ascii_lowercase)]
    return container
