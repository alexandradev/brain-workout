x = input()

if x == 'triangle':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print((p * ((p - a) * (p - b) * (p - c))) ** 0.5)
elif x == 'rectangle':
    a = float(input())
    b = float(input())
    print(a * b)
else:
    x == 'circle'
    r = float(input())
    print(3.14 * (r ** 2))
    
    
