n = int(input())

for i in range(n):
    a, b = [i for i in input().split()]

    print('encaixa' if a[-len(b):] == b else 'nao encaixa')
