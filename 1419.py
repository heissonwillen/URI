number_of_inputs = input()
winners = []

# ['Quico', 'PAR', 'Chiquinha', 'IMPAR']
# ['9', '7']

for number_index in range(int(number_of_inputs)):
    sentence = input().split(' ')
    numbers = input().split(' ')

    numbers = [int(number) for number in numbers]

    for name_index, name in enumerate(sentence):
        if name == 'PAR':
            par_index = name_index - 1
        elif name == 'IMPAR':
            impar_index = name_index - 1

    sum = numbers[0] + numbers[1]

    winners.append(sentence[par_index if sum % 2 == 0 else impar_index])

for winner in winners:
    print(winner)
