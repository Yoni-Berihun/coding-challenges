# You are given an integer n representing the size of an
# array and a list of n integers.

# The array is circular, which means after the last
# element, it wraps around to the first element. For example,
# in a circular array [1, 2, 3], element 3 is followed by 1.

# Find the maximum sum of a subarray that can be for
# med from either a regular subarray or a circular subarray.
# (Circular subarray means you can take elements from the end and
#  continue from the beginning of the array).

# 🧩 Subarray

# A subarray is any contiguous part of the array.

# 📍 Example 1
# Input:
# n = 5
# arr = [8, -1, 3, 4, -2]

# Output:
# 14
# Explanation:
# The maximum sum subarray is [8, -1, 3, 4] = 14.

# 📍 Example 2
# Input:
# n = 4
# arr = [1, -2, 3, -4]

# Output:
# 4
# Explanation:
# The maximum sum subarray is [3] = 3 (but considering circular,
#                                      it wraps to [3, -4, 1]).
# So, sum of [3, -4, 1] = **4**.

# 📍 Example 3
# Input:
# n = 6
# arr = [-2, -3, -1, -4, -6, -5]

# Output:
# -1
# Explanation:
# The maximum subarray sum is just the least negative 
# number, which is -1.