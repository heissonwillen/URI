string_resultado = ''

while True:
    try:
        n, r = [int(i) for i in input().split()]
        identificadores = [int(i) for i in input().split()]

        alguem_morreu = False
        for i in range(1, n+1):
            if i not in identificadores:
                string_resultado += f'{i} '
                alguem_morreu = True

        if not alguem_morreu:
            string_resultado += '* '
            alguem_morreu = False

        string_resultado += '\n'

    except:
        print(string_resultado[:-1])
        break
