def password_validator(*args):
    lis = []
    #is_digit = [False for j in i if not j.isupper() or not j.isupper()]
    alpha = 0
    digit = 0
    #import pdb;pdb.set_trace();
    for i in args[1:]:
        for j in i: # Geek
            c = j.islower() or j.isupper()
            if c:
                if j.isalpha():
                    alpha = 1
            elif j.isdigit():
                digit = 1
            else:
                break
        if alpha == 1 and digit == 1:
            print('String %s is password protected' % i)
            #lis.append(True)
        else:
            print('String %s is not password protected' % i)
            #lis.append(False)
        alpha = 0
        digit = 0
    return lis

password_validator(2, 'Geek', 'GfG1', '1234', '12Gg334', '#$$%%')

