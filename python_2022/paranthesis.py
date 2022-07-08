result = []
number = 3
def generate_para(a=[]):
    if len(a) == 1*number:
        if check_valid(a):
            result.append(''.join(a))

    else:
        #import pdb;pdb.set_trace()
        a.append('(')
        generate_para()
        a.pop()
        a.append(')')
        generate_para()
        a.pop()


def check_valid(a):
    #import pdb;
    #pdb.set_trace();
    bal = 0
    for i in a:
        if i == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            return False
    return bal == 0


generate_para(a=[])

print(result)