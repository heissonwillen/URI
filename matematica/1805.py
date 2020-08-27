soma_ate_n = lambda n: n*(n+1)/2

a, b = [int(i) for i in input().split()]

print(int(soma_ate_n(b)-soma_ate_n(a-1)))
