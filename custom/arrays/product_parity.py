# Product Parity Problem

# You are given an integer n, representing the size of an array, and a list of n integers.

# If the product of all the integers is even, return the sum of the integers.

# If the product of all the integers is odd, return the product of the integers.

# Input

# An integer n

# A list of n integers

# Output

# Return an integer based on the rules above.

# Example 1
# Input:
# n = 3
# Array = [5, 7, 9]

# Output:
# 315

# Example 2
# Input:
# n = 4
# Array = [1, 2, 3, 4]

# Output:
# 10

def function (n,  arr):
    
    total = 0
    product = 1
    has_even = False
    
    for num in arr:
        total += num
        product *= num
        if num % 2 == 0:
            has_even = True
    if has_even:
        return total
    else:
        return product


          
arr = [6, 7, 2]
n = len(arr)

finalvalue = function(n, arr)
print(finalvalue)
    
