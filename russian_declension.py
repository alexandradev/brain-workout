x = int(input())
y = x % 10
z = x % 100
if 11 <= z <= 14:
    print(x, 'программистов')
else:
    if y == 1:
        print(x, 'программист')
    elif 2 <= y <= 4:
        print(x, 'программиста')
    elif 5 <= y <= 9 or y == 0:
        print(x, 'программистов')
    else:
        print('error')
