#Input: digits = "23"
#output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


test = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}


number = str(234)
pp = []

import pdb;pdb.set_trace();
for i in number:
    if test.get(int(i)):
       pp.append(test.get(int(i)))
       #test.pop(int(i))

total = pp.count(pp[0])
for j in range(1, total-1):
    pp.append(pp[0])


final_list = []
another_list = []
print("puneet --> %s" % pp)
for str in pp[1:]:
    for j in str:
        final_list.append(j)
    final_list.append('-')

print("puneet --> %s" % final_list)
for j in pp[0]:
    another_list.append(j)

print("puneet ---> %s" % another_list)

pp = []
for take in another_list:
    try:
        for j in final_list:
            pp.append(take+j)

    except:
        pass




if len(number) == 1:
    print(another_list)
else:
    print(pp)

