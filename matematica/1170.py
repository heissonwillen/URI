n = int(input())

for i in range(n):
    c = float(input())
    d = 0

    while c > 1:
        c /= 2
        d += 1

    print(str(d) + ' dias')
