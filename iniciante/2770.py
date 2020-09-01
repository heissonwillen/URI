while True:
    try:
        x, y, m = [int(j) for j in input().split()]

        for i in range(m):
            x1, y1 = [int(j) for j in input().split()]

            if (x1 <= x and y1 <= y or x1 <= y and y1 <= x):
                print('Sim')
            else:
                print('Nao')
    except EOFError:
        break
