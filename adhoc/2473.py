palavras = ['azar','azar', 'azar', 'terno', 'quadra', 'quina', 'sena',]

flavinho = set([int(i) for i in input().split()])
sorteados = set([int(i) for i in input().split()])

print(palavras[len(flavinho.intersection(sorteados))])
