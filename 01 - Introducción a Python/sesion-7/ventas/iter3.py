def filter(ventas, limite):
    return {month: amount for month, amount in ventas.items() if amount > limite}
