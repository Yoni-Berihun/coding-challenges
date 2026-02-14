# 📄 Problem Question

# You are given an integer n representing the size of an array and a list of n integers.

# If the sum of the integers is divisible by 3, return the maximum value in the array.

# Otherwise, return the minimum value in the array.
#  Input:
# n = 5
# arr = [3, 6, 9, 2, 1]

# Sum = 3 + 6 + 9 + 2 + 1 = 21 (divisible by 3)

# Output:
# 9
# Explanation:
# Sum is divisible by 3 → return maximum value in the array → 9
 
#  Input:
# n = 4
# arr = [4, 5, 7, 2]

# Sum = 4 + 5 + 7 + 2 = 18 (divisible by 3)

# Output:
# 7
# Explanation:
# Sum is divisible by 3 → return maximum value → 7
def function(arr):
    maximum= max(arr)
    print("max", maximum)
    minimum = min(arr)
    print("min", minimum)
    total=0
    for num in arr:
       total += num
    if total % 3 == 0:
           return maximum
    else:
           return minimum
             

arr = [4, 5, 7, 2]
x=function(arr)
print(x)