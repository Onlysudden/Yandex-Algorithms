n = int(input())
r = list(map(int, input().split()))
flag = 0

for i in range(1, len(r)):
    if r[i] < r[i - 1]:
        flag = -1
        break

print(max(r) - min(r) if flag == 0 else flag)
    

