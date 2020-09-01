lista = []

while True:
    try:
        item = input()
        if item not in lista: lista.append(item)
    except EOFError:
        print(len(lista))
        break
