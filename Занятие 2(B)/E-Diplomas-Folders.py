k = int(input())
folders = list(map(int, input().split()))

folders.remove(max(folders))
time = 0

for elem in folders:
    time += elem

print(time)


