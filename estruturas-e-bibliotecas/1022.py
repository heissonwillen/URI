soma =          lambda n_1, n_2 : int(n_1) + int(n_2)
subtrai =       lambda n_1, n_2 : int(n_1) - int(n_2)
multiplica =    lambda n_1, n_2 : int(n_1) * int(n_2)
divide =        lambda n_1, n_2 : int(n_1) / int(n_2)

n_1, o_1, n_2, o_2, n_3, o_3, n_4 = input().split()

print(n_1, o_1, n_2, o_2, n_3, o_3, n_4)

print(soma(n_1, n_2))
