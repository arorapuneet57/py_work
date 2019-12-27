arr = ["geeks", "for", "geeksfor", "geeksforgeeks"]
#arr = ["Hey", "you", "stop", "right", "there"]
temp_str = ''
temp_str1 = ''
flag = 0
arr.sort(reverse=True)
largest_str = arr[0]
arr.remove(largest_str)
for word in arr:
    if word in largest_str:
         temp_str1 = temp_str
         temp_str1 += word
         if temp_str1 in largest_str:
             if temp_str1 == largest_str:
                 break   
    temp_str += str(word)

#if flag == 1:
#   print -1
#else:
print temp_str1
