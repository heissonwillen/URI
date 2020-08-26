forma = lambda a, b, c: True if (abs(b-c)<a and a<b+c) and (abs(a-c)<b and b<a+c) and (abs(a-b)<c and c<a+b) else False
a, b, c, d = [int(i) for i in input().split()]
print('S' if (forma(a, b, c) or forma(a, b, d) or forma(a, c, d) or forma(b, c, d)) else 'N')
