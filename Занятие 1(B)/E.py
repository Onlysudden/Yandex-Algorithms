d = int(input())
x, y = list(map(int, input().split(' ')))

def calc_min(d:int , x:int , y:int) -> int:
    a = ((0 - x) ** 2 + (0 - y) ** 2) ** 0.5
    b = ((d - x) ** 2 + (0 - y) ** 2) ** 0.5
    c = ((0 - x) ** 2 + (d - y) ** 2) ** 0.5
    if a <= b:
        if a <= c:
            return 1
        else:
            return 3
    elif b <= c:
        return 2
    else:
        return 3

if x >= 0 and y >= 0 and (x + y) <= d:
    print(0)
else:
    print(calc_min(d, x, y))
