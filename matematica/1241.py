n = int(input())

def acima_da_media(lista):
    media = sum(lista)/len(lista)
    a = 0
    for item in lista:
        if item > media: a += 1

    return 100*a/len(lista)

for i in range(n):
    lista = [float(i) for i in input().split()]
    lista = lista[1:]

    print(f'{acima_da_media(lista):.3f}%')
