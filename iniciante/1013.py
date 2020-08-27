maior = lambda a, b: int((a+b+abs(a-b))/2)

a, b, c = [int(i) for i in input().split()]

print(f'{maior(maior(a, b), c)} eh o maior')
