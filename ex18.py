import math
angulo = float(input('Qual é o valor do ângulo? '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('SENO DO ÂNGULO {} = {:.2f}'.format(angulo, seno))
print('COSSENO DO ÂNGULO {} = {:.2f}'.format(angulo, cosseno))
print('TANGENTE DO ÂNGULO {} = {:.2f}'.format(angulo, tangente))


#  O algoritmo não funcionava corretamente porque eu não
#  havia convertido o valor de ângulo para radiano