p, n = [int(i) for i in input().split()]
canos = [int(i) for i in input().split()]
game_over = False

for i in range(len(canos)-1):
    if abs(canos[i]-canos[i+1]) > p:
        game_over = True

print('GAME OVER' if game_over else 'YOU WIN')
