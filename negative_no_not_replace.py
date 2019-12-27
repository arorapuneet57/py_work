"""
Input: arr[] = {2, -6, -3, 8, 4, 1}
Output: 1 -6 -3 2 4 8
"""
count = 0
arr=[2, -6, -3, 8, 4, 1]
tarr=list(arr)
arr1 = [None] * len(arr)
for i in arr:
    if i < 0:
        arr1[count] = i
        tarr.remove(i)
    count += 1
tarr.sort()

for num in range(0, len(arr)):
    if arr1[num] is None:
        arr1[num]=tarr[num]
    else:
        tarr.insert(num, 'x')

print arr1
