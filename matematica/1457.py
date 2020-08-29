fatorial = lambda n, k: n*fatorial(n-k, k) if n >= k else k

def quantidade_exclamacoes(l):
    q = 0
    for item in l:
        if item == '!':
            q += 1
    return q

m = int(input())

for i in range(m):
    n = input()
    print(fatorial(int(n.split('!')[0]), quantidade_exclamacoes(n)))
