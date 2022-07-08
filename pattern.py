for i in range(0, 7):
    for j in range(0, i + 1):
        print("*", end='')
    print("\r")



len = 7
count = 0
for i in range(0, 7):
    for j in range(len, i, -1):
        print(' ', end='')
        count = count + 1
    for j in range(0, i+1):
        print('*', end='')
    print("")


k = 3
len = 7
for i in range(0, 7):
    for j in range(len + 2, k, -1):
        print(" ", end='')
    for j in range(0, i):
        print('* ', end='')
    k = k + 1
    print("")
