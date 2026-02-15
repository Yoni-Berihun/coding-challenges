# You are given an integer n representing the size of an 
# array and a list of n integers.

# Count how many positive numbers and negative numbers are 
# in the array.

# If the number of positive elements is greater than 
# negative elements, return the largest element.

# Otherwise, return the smallest element.
# EXAMPLE
# Input:
# n = 6
# arr = [-1, 2, 3, -4, 5, -6]

# Positive count = 3
# Negative count = 3

# Output:
# -6

def function(arr):
    maximumnumber = max(arr)
    minimumnumber = min(arr)
    
    positivecount = 0
    negativecount = 0
    
    for num in arr:
        if num > 0:
            positivecount += 1
        else:
            negativecount += 1
    if positivecount > negativecount:
        return maximumnumber
    else:
        return minimumnumber
    
    
arr = [-1, 2, 3, -4, 5, -6]

x = function(arr)
print(x)
    

