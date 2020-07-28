from random import randint
from time import sleep
gerar_numero = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)

num = int(input('Em que número estou pensando? '))
print('Processando...')
sleep(3)
if num == gerar_numero:
    print('Você venceu!!')
else:
    print('Você perdeu. O número que o computador pensou foi o {}'.format(gerar_numero))