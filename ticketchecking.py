x = int(input())
y = x // 1000
z = x % 1000
a = y // 100
b = (y % 100) // 10
c = (y % 100) % 10
d = z // 100
e = (z % 100) // 10
f = (z % 100) % 10
if a + b + c == d + e + f:
    print('Lucky')
else:
    print('Usual')
