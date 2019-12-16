#### NEED pattern like #####
"""
     *
    ***
   *****
  *******
**********


total_chars = int(raw_input("enter pattern total chars:  " ))
for i in range(0, total_chars):
    for j in range(0, i+1):
        print("* ", end  = ' ')
    print()
"""
def pypart(n): 
      
    # outer loop to handle number of rows 
    # n in this case 
    for i in range(0, n): 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ",end="") 
       
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
pypart(n) 
