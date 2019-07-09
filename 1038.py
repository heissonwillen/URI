cod, q = input().split()
cod, q = int(cod), int(q)
p = 0

if cod == 1:
	p = 4.0
elif cod == 2:
	p = 4.5
elif cod == 3:
	p = 5.0
elif cod == 4:
	p = 2.0
elif cod == 5:
	p = 1.5

print('Total: R$ {:.2f}'.format(q * p))