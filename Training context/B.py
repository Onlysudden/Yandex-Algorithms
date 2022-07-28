n = int(input())

letters = {0: "A", 1: "B", 2: "C", 4: "D", 5: "E", 6: "F"}
places = []

for i in range(n):
    places.append(input())

m = int(input())

members = []

for i in range(m):
    members.append(input().split())

for y in range(m):
    x = "." * int(members[y][0])
    if members[y][1] == "left":
        p1, p2 = 0, int(members[y][0])
        if members[y][2] == "aisle":
            p1, p2 = 3 - int(members[y][0]), 3
    else:
        p1, p2 = 7 - int(members[y][0]), 7
        if members[y][2] == "aisle":
            p1, p2 = 4, 4 + int(members[y][0])

    flag = False

    for i in range(n):
        if places[i][p1:p2] == x:
            flag = True         

            print("Passengers can take seats:", end=' ')
            for j in range(p1, p2-1):
                print(str(i+1) + letters[j], end=' ')
            print(str(i+1) + letters[p2-1])

            for k in range(n):
                if i == k:
                    print(places[k][:p1] + 'X' * (p2 - p1) + places[k][p2:])
                else:
                    print(str(places[k]))
            
            places[i] = places[i][:p1] + '#' * (p2 - p1) + places[i][p2:]
            break

    if not flag:
        print("Cannot fulfill passengers requirements")


