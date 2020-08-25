def remove_duplicatas(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista: nova_lista.append(item)

    return nova_lista

while True:
    try:
        m, n = [int(i) for i in input().split()]
        num_casas_possiveis = 0

        for i in range(m, n+1):
            if list(str(i)) == remove_duplicatas(list(str(i))): num_casas_possiveis += 1

        print(num_casas_possiveis)

    except EOFError:
        break
