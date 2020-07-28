cidade = str(input('Digite o nome de uma cidade: ')).strip()
dividir_cidade = cidade.split()

if dividir_cidade[0] == 'Santo':
    print('O nome da sua cidade começa com a palavra SANTO')
else:
    print('O nome da sua cidade não começa com a palavra SANTO')
