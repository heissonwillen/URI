import math

while True:
    if int(input()) == 0: break

    lista = [int(i) for i in input().split()]

    resultado = [lista[0]+lista[-1], lista[math.ceil(len(lista)/2)-1]+lista[math.ceil(len(lista)/2)]]

    resultado.sort(reverse=True)

    print(f'{resultado[0]} {resultado[1]}')
