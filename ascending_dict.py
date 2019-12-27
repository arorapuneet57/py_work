"""
Input : {1: 'puneet', 4: 'rahul', 10: 'fargo'} 
output: {10: 'fargo', 1: 'puneet', 4: 'rahul'}
"""
from collections import OrderedDict 

my_dict = {1: 'puneet', 4: 'rahul', 10: 'fargo', 0 : 'skyline', -1 : 'Arc'}
values_list = my_dict.values()
values_list.sort()

new_dict = OrderedDict()
for i in values_list:
    for j in my_dict.keys():
        if i == my_dict[j]:
            new_dict[j] = i
            break
print new_dict
