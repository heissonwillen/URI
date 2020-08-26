n = int(input())

lista = [i for i in input().split()]

maior = anterior = 0

lista.append(' ')

for i in range(1, len(lista)):
    if lista[i-1] == lista[i]:
        anterior += 1
    else:
        if anterior > maior: maior = anterior
        anterior = 0

print(maior+1)
