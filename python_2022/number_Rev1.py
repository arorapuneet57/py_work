def reverse(x):
    l = ''
    flag = False
    if x < 0:
        x = abs(x)
        if x < 2147483647:
            flag = True
        else:
            return 0
    import pdb;pdb.set_trace();
    if x > 0 and x < 2147483647:
        while x > 0:
            l = l + str(x % 10)
            x = int(x / 10)
        if int(l) > 2147483647:
            return 0
        if flag:
            return -(int(l))
        else:
            return int(l)
    else:
        if x == 0 or x <= 2147483647:
            return 0
        return -1


out = reverse(-2147483648)
print(out)