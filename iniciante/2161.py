n = int(input())

x = 0

for i in range(n):
    x += 6
    x = 1/x

x+= 3

print(f'{x:.10f}')
