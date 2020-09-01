n = int(input())

carrinhos = bonecas = 0

for i in range(n):
    _, s = input().split()

    if s == 'M': carrinhos += 1
    elif s == 'F': bonecas += 1

print(f'{carrinhos} carrinhos')
print(f'{bonecas} bonecas')
