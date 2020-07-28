qt_carteira = float(input('Quantos reais você tem dentro da carteira? R$ '))
qt_dolar = qt_carteira / 5.32
print(f"Você pode comprar ${round(qt_dolar, 2)} americanos")
