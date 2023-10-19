r = 5
for i in range(r, 0, -1):
    for j in range(1,i):
        print(end = " ")
    for k in range(i, r+1):
        print(k, end = " ")
    print(" ")