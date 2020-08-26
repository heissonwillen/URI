while True:
    try:
        h, m = [int(i) for i in input().split()]

        print(f'{str(int(h*12/360)).zfill(2)}:{str(int(m*60/360)).zfill(2)}')

    except EOFError:
        break
