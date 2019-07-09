n = int(input())

inside = outside = 0
 
for i in range (n):
	x = int(input())

	if (x >= 10 and x <= 20):
		inside += 1
	else:
		outside += 1

print('{} in\n{} out'.format(inside, outside))