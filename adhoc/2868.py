n = int(input())

def operacao(sinal):
    if sinal == '+':
        return lambda a, b: a + b
    elif sinal == '-':
        return lambda a, b: a - b
    elif sinal == 'x':
        return lambda a, b: a * b
    elif sinal == '/':
        return lambda a, b: a / b
    else:
        return None


for i in range(n):
    a, sinal, b, _, resultado = input().split()

    print('E', end='')
    for j in range(abs(operacao(sinal)(int(a), int(b)) - int(resultado))):
        print('r', end='')
    print('ou!')
