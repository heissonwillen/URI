n = int(input())

print('Farei hoje!' if sum([int(i) for i in input().split()]) <= n else 'Deixa para amanha!')
