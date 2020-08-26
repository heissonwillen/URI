n = int(input())
estrelas = [0] + [int(i) for i in input().split()] + [0]

i = 1

atacadas = [0 for i in range(len(estrelas) + 2)]

while True:
    estrelas[i] -= 1

    if estrelas[i]%2 == 0 and estrelas[i+1] > 0:
        i += 1
        atacadas[i] = 1
    elif estrelas[i]%2 != 0 and estrelas[i-1] > 0:
        atacadas[i] = 1
        i -= 1
    else:
        break

print('{} {}'.format(sum(estrelas), sum(atacadas)+1))
