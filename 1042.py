a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

x, y, z = a, b, c

if (a < b):
	a, b = b, a

if (b < c):
	b, c = c, b

if (a < b):
	a, b = b, a

print('{}\n{}\n{}'.format(c, b, a))
print('\n{}\n{}\n{}'.format(x, y, z))