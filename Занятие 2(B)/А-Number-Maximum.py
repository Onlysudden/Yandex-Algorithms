max = 0
count = 0

while True:
    elem = int(input())
    if elem != 0:
        if elem > max:
            max = elem
            count = 1
        elif elem == max:
            count += 1
    else:
        break

print(count)