actions = 'OL; bmap:0x12000c0 inval(s):132 cg:322 dp:0x4 len:704; DFW on srcPort, ctCtxId: 0x2; VNI: 69632; DFW on dstPort, ctCtxId: 0x3;   1  0'

output = actions.strip('\n').split()
print(output[-2])


import re
out = "Puneet"
p = re.search(r'ku', out) and re.search(r'xu', out)
if p:
    print("out")


def sort(first, item, len, last, to_search):
     if first < len :
        pivot = int((first + len)/ 2)
        if item[first] < to_search:
            print(item[first])
            first = pivot
            sort(first, item, len, last, 4)
        if item[first] > to_search:
            last = pivot
            print(item[last])
            sort(first, item, len, last, 4)
        if item[first] == to_search or item[last] == to_search:
            print('hi')

sort(0, [1,3,4,5,6], len([1,3,4,5,6]), 5, 4)





