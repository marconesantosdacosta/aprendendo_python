q = float(input('Vazão: '))
i = float(input('Declividade: '))
z = float (input('Z: '))
n = float(input ('Coeficiente de manning: '))

y = q/(0.375*pow(i,0.5)*(z/n))
y1 = pow(y,(3/8))

print ('lamina da dagua = {}' .format(y1))