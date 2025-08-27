print (' CALCULO DA INTENSIDADE DA CHUVA')
print('')
print('DADOS DO PLUVIO')

k = float(input('k: '))
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

print('')
tr = float(input('Tempo de retorno: '))
t = float (input ('tempo de concentração: '))
x = t + b

i = (k*pow(tr, a))/pow(x,c)

print('INTENSIDADE DA CHUVA: {}' .format(i))