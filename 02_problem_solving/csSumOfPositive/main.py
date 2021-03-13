# Given an array of integers, return the sum of all the positive integers in the array.
#
# Examples:
#     csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
#
#If the input_arr does not contain any positive integers, the default sum should be 0.

def csSumOfPositive(input_arr):
    count = 0
    
    for n in input_arr:
        if n > 0:
            count += n
    return count

print(csSumOfPositive([1, 2, 3, -4, 5]))