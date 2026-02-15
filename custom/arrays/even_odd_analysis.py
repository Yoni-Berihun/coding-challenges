# 📄 Problem Statement

# You are given an integer n representing the size of an
# array and a list of n integers.

# Count how many numbers in the array are even and 
# how many are odd.

# Find the sum of even numbers and the sum of odd numbers.

# Apply the following rules:

# If the count of even numbers is greater than the count of 
# odd numbers, return the sum of even numbers.

# If the count of odd numbers is greater than the count of
# even numbers, return the sum of odd numbers.

# If the counts are equal, return the difference between the 
# larger sum and the smaller sum.

# Example Test Case 1:
    
# Input:
# n = 6
# arr = [2, 4, 6, 1, 3, 5]

# Even count = 3
# Odd count = 3
# Even sum = 12
# Odd sum = 9

# Output:
# 3

# Example 2
# Input:
# n = 5
# arr = [2, 8, 1, 3, 5]

# Even count = 2
# Odd count = 3
# Odd sum = 9

# Output:
# 9

# Example 3
# Input:
# n = 4
# arr = [10, 2, 8, 6]

# Even count = 4
# Odd count = 0
# Even sum = 26

# Output:
# 26
def function(arr):
    evencount = 0
    oddcount = 0
    sumofeven = 0
    sumofodd = 0
    
    for num in arr:
        if num % 2 == 0:
            evencount += 1
            sumofeven += num
        else:
            oddcount += 1
            sumofodd += num
    if evencount > oddcount:
        return sumofeven
    if oddcount >evencount:
        return sumofodd
    else:
        if sumofeven > sumofodd:
            return sumofeven - sumofodd
        else:
            return sumofodd - sumofeven
        

arr = [2, 4, 6, 1, 3, 5]

x = function(arr)
print(x)