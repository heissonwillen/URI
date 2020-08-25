def soma_lista(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma

lista_renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

lista_bolas = [int(i) for i in input().split()]

print(lista_renas[soma_lista(lista_bolas)%len(lista_renas)-1])
