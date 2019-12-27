"""
Input : {1: 'puneet', 4: 'rahul', 10: 'fargo'} 
output: {10: 'fargo', 1: 'puneet', 4: 'rahul'}
"""
from collections import OrderedDict 
final_dict = OrderedDict()
my_dict = {1: 'puneet', 4: 'rahul', 10: 'fargo', 0 : 'skyline', -1 : 'Arc'}

new_dict = dict([(values,key) for key,values in my_dict.items()])
print new_dict
for i in sorted(new_dict):
    final_dict[i] = new_dict[i]
print final_dict
