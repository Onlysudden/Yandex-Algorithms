x = str(input())
cost = 0

if len(x) == 1:
    print(0)
else:
    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            cost += 1
    print(cost)
