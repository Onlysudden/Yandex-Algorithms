d, m, y = map(int, input().split(" "))

if (d > 12 and m <= 12) or (d <= 12 and m > 12) or (d == m and d <= 12):
    print(1)
else:
    print(0)