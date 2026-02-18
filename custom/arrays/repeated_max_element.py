# You are given an array of integers.

# Find the largest element in the array.

# Count how many times this largest element appears.

# If the largest element appears more than once, return that element.

# Otherwise, return -1.

# 📌 Examples
# Example 1
# Input:
# arr = [1, 3, 5, 5, 2]

# Largest element = 5
# Count = 2

# Output:
# 5

# Example 2
# Input:
# arr = [4, 2, 1]

# Largest element = 4
# Count = 1

# Output:
# -1

# Example 3
# Input:
# arr = [7, 7, 7]

# Largest element = 7
# Count = 3

# Output:
# 7


def function(arr):
    count = 0
    maximum = max(arr)
    for num in arr:
        if num == maximum:
            count+=1
    if count > 1:
        print( max(arr))
    else:
        print(-1)
    
arr = [7, 7, 7]
function(arr)