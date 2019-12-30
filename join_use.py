"""
   Input : ['geeks', 'for', 'geeks']
   Output : geeks for geeks
"""
ss = ''
li = ['pp', 'll', 'dd']
#print str(li).translate(None, '[],'')
q = '1'.join(li)
print q
for i in li:
    ss = ss + ' ' + i

print ss
