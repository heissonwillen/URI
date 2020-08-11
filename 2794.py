n, l = int(input()), []

for i in range(n):
    l.append(tuple([int(item) for item in input().split()]))

l.sort()

renato_esta_certo = True
for i in range(1, len(l)):
    if l[i][1] > l[i-1][1]:
        renato_esta_certo = False

print("S" if renato_esta_certo else "N")
