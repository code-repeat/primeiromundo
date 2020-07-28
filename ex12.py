preco = float(input('Informe o preço do produto: '))
tax_desc = 5

novo_preco = preco - (preco * tax_desc / 100)
print("O preço do produto com {}% é R${:.2f}".format(tax_desc, novo_preco))
