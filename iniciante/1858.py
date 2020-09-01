_ = int(input())

menor = 21

numeros = [int(i) for i in input().split()]

for i, numero in enumerate(numeros):
    if numero < menor:
        menor = numero
        indice_menor = i+1

print(indice_menor)
