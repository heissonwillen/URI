fatorial = lambda n: 1 if n == 0 else n*fatorial(n-1)

while True:
    n = list(input())

    if n[0] == '0': break

    soma, aux = 0, len(n)

    for i in range(aux):
        soma += int(n[i]) * fatorial(aux)
        aux -= 1

    print(soma)
