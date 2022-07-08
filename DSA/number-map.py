test = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

global list_results
list_results = []
number = str("")
telephone = []
li = []
pi =[]
out= []




def accumulate_number(str1):

    temp_results = []
    global list_results
    if list_results:
        for j in list_results:
            for k in str1:
                final_str = k + j
                temp_results.append(final_str)
        list_results = temp_results
        return list_results


    else:
        for k in str1:
            list_results.append(k)


for num in number:
    if test.get(int(num)):
       telephone.append(test.get(int(num)))

total_numbers_count = len(telephone)

for num in range(total_numbers_count, -1, -1):
    try:
        import pdb;pdb.set_trace()
        accumulate_number(telephone[num])
        #print(list_results)
    except:
        pass
print(list_results)

"""
def second(str1, str2):
    for j in str1:
        final_str = j + str2
        pi.append(final_str)
    return pi

for num in number:
    if test.get(int(num)):
       telephone.append(test.get(int(num)))



total_numbers_count = len(telephone)
final_str = accumulate_number(telephone[total_numbers_count-1], telephone[total_numbers_count-2])

print(final_str)
import pdb;pdb.set_trace();
for l in final_str:
    print(l)
    out.append(second(telephone[0], l))

print(out[0])
"""
