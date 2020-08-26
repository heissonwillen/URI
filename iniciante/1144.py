n = int(input())

a = b = 1

for i in range(1, n+1):
    print(f'{i} {a} {b}')
    a += 1
    b += 1
    print(f'{i} {a} {b}')
    a += i+1
    b += i+2
