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

#we will use kadane's algortm here:
# The problem: Find the contiguous subarray
# (a continuous slice of the array) that has
# the largest possible sum.

# The idea:

# Keep a running sum (maxEndingHere) as you move through the array.

# If this running sum ever becomes negative, reset 
# it to 0 — because carrying a negative sum forward 
# will only hurt future totals.

# Keep track of the best sum you’ve seen so far (maxSoFar).

# The result: At the end, maxSoFar holds the 
# maximum subarray sum.


def maxCircularSubarray(arr):
    n = len(arr)
    
    # --- 1. Normal Kadane (max subarray) ---
    max_sum = arr[0]
    current_sum = 0
    start = end = temp_start = 0

    for i in range(n):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    normal_subarray = arr[start:end+1]

    # --- 2. Find minimum subarray (for circular case) ---
    min_sum = arr[0]
    current_min = 0
    start_min = end_min = temp_start_min = 0

    for i in range(n):
        current_min += arr[i]

        if current_min < min_sum:
            min_sum = current_min
            start_min = temp_start_min
            end_min = i

        if current_min > 0:
            current_min = 0
            temp_start_min = i + 1

    total_sum = sum(arr)
    circular_max_sum = total_sum - min_sum

    # --- 3. Handle all-negative array ---
    if max_sum < 0:
        return max_sum, normal_subarray

    # --- 4. Decide which is better ---
    if circular_max_sum > max_sum:
        # Circular subarray elements: outside the min subarray
        circular_subarray = arr[end_min+1:] + arr[:start_min]
        return circular_max_sum, circular_subarray
    else:
        return max_sum, normal_subarray

arr = [8, -1, 3, 4, -2]
max_sum, subarr = maxCircularSubarray(arr)
print("Maximum Sum:", max_sum)
print("Subarray:", subarr)
