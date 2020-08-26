def soma_lista(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma


notas = [float(i) for i in input().split()]

notas.sort()

print(f'{soma_lista(notas[1:-1]):.1f}')
