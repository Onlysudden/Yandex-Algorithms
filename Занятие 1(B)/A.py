r, i, c = (int(input()) for j in range(3))
true_set = {0, 1, 4, 6, 7}

if i in true_set:
    if i == 0 and r != 0:
        print(3)
    elif i == 1:
        print(c)
    elif i == 4 and r != 0:
        print(3)
    elif i == 6:
        print(0)
    elif i == 7:
        print(1)
    elif r == 0:
        if i == 0:
            print(c)
        else:
            print(4)
else:
    print(i)
    

