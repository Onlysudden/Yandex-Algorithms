line = list(map(int, input().split()))

max = 0
for i in range(len(line)):
    if line[i] == 1:
        min = 10
        for j in range(len(line)):
            if line[j] == 2:
                d = abs(j - i)
                if d < min:
                    min = d
        if min > max:
            max = min

print(max)

