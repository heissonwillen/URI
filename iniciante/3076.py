import math

while True:
    try:
        print(math.ceil(int(input())/100))
    except EOFError:
        break
