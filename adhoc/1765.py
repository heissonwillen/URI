H = 5

while True:
    t = int(input().split(' ')[0])
    if t == 0: break
    for i in range(t):
        q, a, b = [float(item) for item in input().split()]
        print(f'Size #{i+1}:\nIce Cream Used: {(q*H*(a+b)/2):.2f} cm2')

    print()
