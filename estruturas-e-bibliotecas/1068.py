expressao = input()

num_abertos, num_fechados = 0, 0

for caractere in expressao:
    if caractere == '(':
        num_abertos += 1
    if caractere == ')':
        num_fechados += 1
