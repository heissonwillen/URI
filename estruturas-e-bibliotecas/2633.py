while True:
    try:
        n = int(input())
        lista = []

        for i in range(n):
            carne, validade = input().split()
            lista.append({
                'carne': carne,
                'validade': int(validade)
            })

        lista.sort(key=lambda item: item['validade'])

        for item in lista:
            print(item['carne'], end=' ')

    except EOFError:
        break
