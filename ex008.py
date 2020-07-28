valor_metro = float(input('Digite alguma distância em metros: '))
cm = valor_metro * 100
mm = valor_metro * 1000
dam = valor_metro / 10
hm = valor_metro / 100
km = valor_metro / 1000
#  saída refatorada
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(valor_metro, cm, mm))
print('A mesma mediada em {}dam, {}hm e {}km'.format(dam, hm, km))
