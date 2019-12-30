"""
Input='Geeks'
Output=['G', 'Ge', 'Gee', 'Geek', 'Geeks', 'e', 'ee', 'eek', 'eeks', 'e', 'ek', 'eks', 'k', 'ks', 's']
"""
k= ''
count = 0 
pl = []
g_str = 'Geeks'
p_str = g_str[count:len(g_str)]
while(True):
    try:
         if p_str.endswith(p_str[len(p_str)-1]) == True:
              p_str = g_str[count:len(g_str)]
              for i in p_str:
                  for j in i:
                      k = k + j
                      pl.append(k)
              k = ''
              count += 1
         else:
             break
    except IndexError:
        break
print pl
