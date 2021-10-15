a, b, c = [int(x) for x in input().split()]
x, y, z = [int(x) for x in input().split()]
n1 = z//c
n2 = y//b
n3 = x//a
n =n1 * n2 *n3
print(n)
