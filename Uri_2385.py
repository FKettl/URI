n = int(input())
p, q, r, s, x, y = [int(x) for x in input().split()]
linha, coluna = [int(x) for x in input().split()]

c = 0
for z in range (1, n+1):
    a =  ((p*linha)+(q*z))%x
    b =  ((r*z)+(s*coluna))%y
    c += a*b

print(c)