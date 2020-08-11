def val_abs(n):
    return (-n if n < 0 else n)

while True:
    x_1, y_1, x_2, y_2 = [int(coord) for coord in input().split()]

    if x_1 == 0 and y_1 == 0 and x_2 == 0 and y_2 == 0:
        break

    distancia_x = val_abs(x_1 - x_2)
    distancia_y = val_abs(y_1 - y_2)

    if distancia_x and distancia_y > 0:
        if distancia_x == distancia_y:
            num_movimentos = 1
        else:
            num_movimentos = 2
    else:
        num_movimentos = 0

    print(num_movimentos)
