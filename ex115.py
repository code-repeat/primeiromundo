km = float(input('Quantos km você percorridos? '))
dias = int(input('Por quantos dias o carro esteve alugado? '))
aluguel = 60 * dias
preco_final = (km * 0.15) + aluguel
print("TOTAL A PAGAR: R${:.2f}".format(preco_final))