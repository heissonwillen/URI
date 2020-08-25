X = 20001

lista = [0 for item in range(1, X+1)]

n = int(input())

for i in range(n):
    lista[int(input().split()[0])] += 1

for i in range(1, X):
    if lista[i] > 0: print(f'{i} aparece {lista[i]} vez(es)')
