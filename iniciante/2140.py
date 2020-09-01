while True:
    n, m = [int(i) for i in input().split()]

    if n == 0 or m == 0: break

    eh_possivel = False

    if (m-n)%2 == 0 or (m-n)%5 == 0 or ((m-n)%5)%2: eh_possivel = True

    print('possible' if eh_possivel else 'impossible')
