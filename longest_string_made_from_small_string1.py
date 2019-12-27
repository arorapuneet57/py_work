def sample(temp_str, sample_str, temp_str1):
    for word in arr:
        if word in largest_str:
             sample_str = temp_str1
             temp_str1 = temp_str
             temp_str1 += word
             if temp_str1 in largest_str:
                 if temp_str1 == largest_str:
                     return temp_str1
                 else:
                     temp_str += str(word)
             else:
                 temp_str = sample_str

if __name__ ==  "__main__":
#    arr = ["geeks", "for", "geeksfor", "geeksforgeeks"]
#    arr = ["puneet", "arora", "ar", "hero", "puneetarora"]
    import pdb;pdb.set_trace();
    arr = ["anupriya", "zrora", "anupriyazrora" , " proma", "aroma", "champu", "fuddu"]
    #arr = ["Hey", "you", "stop", "right", "there"]
    temp_str = ''
    temp_str1 = ''
    sample_str = ''
    largest_str = max(arr, key=len)
    arr.remove(largest_str)
#    arr.sort(reverse=True)
#    largest_str = arr[0]
#    arr.remove(largest_str)
    pp = sample(temp_str, sample_str, temp_str1)
    if pp:
        print pp
    else:
        print -1
