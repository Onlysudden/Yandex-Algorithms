l, c = list(map(int, input().split()))
numbers = list(map(int, input().split()))
left_list = []
right_list = []
flag = True

if l % 2 != 0:
    for elem in numbers:
        if elem == (l // 2):
            print(elem)
            flag = False
        else:
            if elem < (l // 2):
                left_list.append(elem)
            else:
                right_list.append(elem)
    if flag is True:
        print(max(left_list), min(right_list))
else:
    for elem in numbers:
        if elem < (l // 2):
            left_list.append(elem)
        else:
            right_list.append(elem)
    print(max(left_list), min(right_list))