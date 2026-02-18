# Array Problems Journal

This document tracks my progress, learnings, and time spent on array-based coding challenges.

## Progress Overview
| Date | Problem | Time Spent | Key Concepts |
|---|---|---|---|
| Feb 13, 2026 | [Product Parity](../custom/arrays/product_parity.py) | ~2 hours | Initialization, Loops, Indentation |
| Feb 14, 2026 | [Sum Divisible By Three](../custom/arrays/sum_divisible_by_three.py) | 1h 20m | Basic DS, Iteration, Loops |
| Feb 15, 2026 | [Positive Negative Count](../custom/arrays/positive_negative_count.py) | ~40 mins | Control Flow, Conditionals |
| Feb 15, 2026 | [Even Odd Analysis](../custom/arrays/even_odd_analysis.py) | ~30 mins | Counting + Summing, Nested Conditionals, Decision Logic |
| Feb 16, 2026 | [Maximum Circular Subarray Sum](../custom/arrays/maximum_circular_subarray_sum.py) | ~8 hours | Kadane’s Algorithm, Circular Arrays, Edge Cases, Needs Reinforcement |
| Feb 18, 2026 | [Repeated Max Element](../custom/arrays/repeated_max_element.py) | 10 mins | Max + Count, Frequency |

---

## Detailed Logs

### 1. Product Parity
**File:** `custom/arrays/product_parity.py`
**Date:** February 13, 2026
**Time Spent:** ~2 hours

**Key Learnings:**
1.  **Array Initialization**: 
    - Understood how to create arrays/lists in Python.
    - Learned to use `len()` instead of `.__len__`.
2.  **Looping & Logic**: 
    - Practiced iterating through lists to calculate sums and products.
    - Learned how to check for even numbers using `% 2`.
3.  **Syntax & Debugging**: 
    - **Indentation**: Realized the importance of matching indentation levels for `if` statements inside/outside loops.
    - **Persistence**: Spent time debugging specific syntax errors, which reinforced the rules of the language.

### 2. Sum Divisible By Three
**File:** `custom/arrays/sum_divisible_by_three.py`
**Date:** February 14, 2026
**Time Spent:** 1 hour 20 mins

**Key Learnings:**
1.  **Data Structures**: 
    - Solidified understanding of arrays as the fundamental data structure for storing collections of items.
2.  **Iteration**: 
    - Practiced iterating through array elements to perform operations on each item.
3.  **Troubleshooting**: 
    - **Indentation (Again)**: Encountered challenges with Python's indentation rules, specifically when nesting logic inside loops.
    - **Task Execution**: Learned to distinguish between actions that happen *during* the loop versus *after* the loop completes.

### 3. Positive Negative Count
**File:** `custom/arrays/positive_negative_count.py`
**Date:** February 15, 2026
**Time Spent:** ~40 mins

**Key Learnings:**
1.  **Control Flow**:
    - Gained a solid understanding of how `if` and `else` statements work within loops.
    - Used conditional logic to categorize numbers (positive vs negative).
2.  **Built-in Functions**:
    - Utilized `max()` and `min()` functions effectively to find extremes in the array.
3.  **Logic Implementation**:
    - Successfully implemented logic to compare counts and return different results based on the comparison.

### 4. Even Odd Analysis
**File:** `custom/arrays/even_odd_analysis.py`
**Date:** February 15, 2026
**Time Spent:** ~30 mins

**Key Learnings:**
1.  **Two-Phase Pattern (Aggregate → Decide)**:
    - Phase 1: compute facts in a single loop (even/odd counts + sums).
    - Phase 2: apply rules with a clean decision tree.
2.  **Nested Conditionals (but keep them readable)**:
    - If branches are mutually exclusive, prefer `if / elif / else` instead of multiple `if` statements.
3.  **Simplifying “equal counts” logic**:
    - When counts are equal, the answer is just the absolute difference between sums:
      - `abs(sum_even - sum_odd)`
4.  **Refactor idea (same logic, cleaner)**:
    - Keep the computation the same, but the return logic can be compact:
      - If `even_count > odd_count`: return `sum_even`
      - Else if `odd_count > even_count`: return `sum_odd`
      - Else: return `abs(sum_even - sum_odd)`

*Note: Debugging simple syntax errors is part of the process!*

### 5. Maximum Circular Subarray Sum
**File:** `custom/arrays/maximum_circular_subarray_sum.py`
**Date:** February 16, 2026
**Time Spent:** ~8 hours (total)
**Status:** Needs reinforcement

**Key Learnings:**
1. **Kadane’s algorithm is the core building block** for finding the max sum over any contiguous subarray.
2. **Circular trick idea** (still working through it):
    - Best circular sum often equals `total_sum - (minimum subarray sum)`.
3. **Important edge case**:
    - If all numbers are negative, the answer is the maximum (least negative) single element (and the circular trick can give 0, which would be wrong).

---

## Kadane’s Algorithm (Max Subarray Sum) — Theory Only

Core idea (non-circular):
- Track two values while scanning left to right:
    - `maxEndingHere`: best sum ending at current index → `max(arr[i], maxEndingHere + arr[i])`.
    - `maxSoFar`: global best so far → `max(maxSoFar, maxEndingHere)`.
- Complexity: O(n) time, O(1) space.

Circular variant (wrap-around allowed):
- Let `maxNormal` be the standard Kadane result.
- Let `total` be the sum of all elements.
- Let `minSubarray` be the minimum contiguous subarray sum (compute via Kadane on inverted values or by tracking minimum instead of maximum).
- Candidate circular sum is `total - minSubarray` (this picks a prefix and suffix by excluding the worst middle segment).
- Final answer: $
    	ext{maxCircular} = \begin{cases}
        \max(\text{maxNormal}, \; \text{total} - \text{minSubarray}) & \text{if } \text{maxNormal} \ge 0 \\
        	ext{maxNormal} & \text{if all elements are negative}
    \end{cases}
    $

Practical notes:
- If all numbers are negative, `total - minSubarray` becomes 0; ignore it and return `maxNormal` (the least negative element).
- When multiple subarrays tie, any one is acceptable unless the problem specifies otherwise.

### Python (reference implementation)

```python
from typing import List

def kadane_max(arr: List[int]) -> int:
    """Standard Kadane's algorithm: maximum subarray sum."""
    max_ending = arr[0]
    max_so_far = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far

def kadane_min(arr: List[int]) -> int:
    """Minimum subarray sum using Kadane-like traversal."""
    min_ending = arr[0]
    min_so_far = arr[0]
    for x in arr[1:]:
        min_ending = min(x, min_ending + x)
        min_so_far = min(min_so_far, min_ending)
    return min_so_far

def max_circular_subarray_sum(arr: List[int]) -> int:
    """
    Maximum subarray sum allowing wrap-around.
    - If all numbers are negative, returns the largest (least negative) element.
    - Otherwise, compares normal Kadane vs circular candidate (total - minSubarray).
    """
    if not arr:
        return 0
    max_normal = kadane_max(arr)
    if max_normal < 0:
        return max_normal
    total = sum(arr)
    min_sub = kadane_min(arr)
    return max(max_normal, total - min_sub)
```

### 6. Repeated Max Element
**File:** `custom/arrays/repeated_max_element.py`
**Date:** February 18, 2026
**Time Spent:** 10 minutes

**Problem:** Given an integer array, find the largest element and count its occurrences. If it appears more than once, return the element; otherwise, return -1.
**Notes:**
- Single linear scan for counting; overall O(n) time, O(1) extra space.
- Handles empty arrays explicitly; original script printed results, this version returns a value for reuse.

