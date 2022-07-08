from collections import OrderedDict
dic = {3: 'z',  5: 'c', 1: 'd', 100: 'a'}
print("Dict provided  %s" % dic)

new_dic = OrderedDict()
new_dic = {}
for x, y in dic.items():
    new_dic[y] = x
print("dict after first change %s" % new_dic)


li = [ x for x in new_dic.keys()]
li.sort()

dic = OrderedDict()
dic = {}
for i in li:
    dic[i] = new_dic[i]
print("Dict after sort %s" % dic)

new_dic = OrderedDict()
new_dic = {}
for x, y in dic.items():
    new_dic[y] = x

print("dict after all change %s" % new_dic)


