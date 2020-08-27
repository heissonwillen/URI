fatorial = lambda n: 1 if n == 0 else n*fatorial(n-1)

while True:
    try:
        lista = [fatorial(int(i)) for i in input().split()]
        print(sum(lista))
    except EOFError:
        break
