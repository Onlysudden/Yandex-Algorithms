l, c = list(map(int, input().split()))
numbers = list(map(int, input().split()))
l_list = []
r_list = []
flag = True

if l % 2 != 0:
    for elem in numbers:
        if elem == (l // 2):
            print(elem)
            flag = False
        else:
            if elem < (l // 2):
                l_list.append(elem)
            else:
                r_list.append(elem)
    if flag is True:
        print(max(l_list), min(r_list))
else:
    for elem in numbers:
        if elem < (l // 2):
            l_list.append(elem)
        else:
            r_list.append(elem)
    print(max(l_list), min(r_list))