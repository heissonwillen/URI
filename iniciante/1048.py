sal = float(input())

novoSal = 0
reajuste = 0
percentual = 0

if (sal <= 400):
	percentual = 0.15
elif (sal > 400 and sal <= 800):
	percentual = 0.12
elif (sal > 800 and sal <= 1200):
	percentual = 0.10
elif (sal > 1200 and sal <= 2000):
	percentual = 0.07
elif (sal > 2000):
	percentual = 0.04

reajuste = sal * percentual
novoSal = sal + reajuste

print('Novo salario: {:.2f}'.format(novoSal))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(int(percentual * 100)))