"""
Input: arr[] = {5, 10, 5, 7, 4, 3, 5}
Output:
Peaks : 10 7 5
Troughs : 5 5 3
"""
arr1 = []
arr = [5, 10, 5, 7, 4, 3, 5, 2, 5, 3, 1, 10, 11, 100, 3, 20]
# check peak elmement
count = 0
for i in arr:
    if count != len(arr)-1:
        if count == 0 and i > arr[count+1]:
            arr1.append(i)
        if i > arr[count+1] and i > arr[count-1]:
            arr1.append(i)
    else:
        if arr[count] > arr[count-1]:
            arr1.append(i)
        break
    count += 1 
print arr1

# check throuh element
count = 0
arr2 = []
for i in arr:
    if count != len(arr)-1:
        if count == 0 and i < arr[count+1]:
            arr2.append(i)
        if i < arr[count+1] and i < arr[count-1]:
            arr2.append(i)
    else:
        if arr[count] < arr[count-1]:
            arr2.append(i)
        break
    count += 1 
print arr2
