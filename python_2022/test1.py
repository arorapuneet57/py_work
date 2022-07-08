"""
Given a set of coins, there are some arnounts of change that you may not be able to make with them, e.9., you cannot create a change amount greater than the sum of the your coins. For example, if your coins are 1,1.,1,1.,1.,5,10,25, then the smallest value of change which cannot be made is 21.
Write a program which takes an array of positive integers and retums the smallest number which is not to the sum of a subset of elements of the array.
"""

#input = [1,1,1,1,1,5,10,25,]
input = [12,2,1,15,2,4]

input.sort()
add_appr_value = 1
for coin in input:
    test_value = add_appr_value
    if coin > test_value:
        print(test_value)
        break

    add_appr_value += coin


