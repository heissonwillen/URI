n, campo = int(input()),  []

bombas_vizinhanca = [0 for i in range(n)]

for i in range(n):
    campo.append(int(input()))

for i, mina in enumerate(campo):
    if i == 0:
        if len(campo) > 0:
            bombas_vizinhanca[i] = campo[i]+campo[i+1]
        else:
            bombas_vizinhanca[i] = campo[i]
    elif i == len(campo)-1:
        bombas_vizinhanca[i] = campo[i-1]+campo[i]
    else:
        bombas_vizinhanca[i] = campo[i-1]+campo[i]+campo[i+1]

for bomba in bombas_vizinhanca:
    print(bomba)
