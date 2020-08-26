n = int(input())
A = 2015

for i in range(n):
    y = int(input())
    print(str(A-y)+' D.C.' if y<A else str(-(A-y-1))+' A.C.')
