quarters = {
    'Q1': [],
    'Q2': [],
    'Q3': [],
    'Q4': [],
}

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

quarters_data = [
    ["Enero", "Febrero", "Marzo"],
    ["Abril", "Mayo", "Junio"],
    ["Julio", "Agosto", "Septiembre"],
    ["Octubre", "Noviembre", "Diciembre"],
]

for index, meses in enumerate(quarters_data):
    quarter = index + 1
    for mes in meses:
        quarters['Q{}'.format(quarter)].append(ventas[mes])

print(quarters)

'''
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
for indice_mes, mes in enumerate(meses):
    if mes in ventas:
        quarter = int(indice_mes / 3) + 1
        quarters['Q{}'.format(quarter)].append(ventas[mes])
'''
