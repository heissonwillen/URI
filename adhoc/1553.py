while True:
    n, k = [int(i) for i in input().split()]

    if n == 0 or k == 0: break

    perguntas = [int(i) for i in input().split()]

    print(f'n, k: {n, k}')
    print(f'perguntas: {perguntas}')
