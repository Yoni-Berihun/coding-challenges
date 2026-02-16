# Array Problems Journal

This document tracks my progress, learnings, and time spent on array-based coding challenges.

## Progress Overview
| Date | Problem | Time Spent | Key Concepts |
|---|---|---|---|
| Feb 13, 2026 | [Product Parity](../custom/arrays/product_parity.py) | ~2 hours | Initialization, Loops, Indentation |
| Feb 14, 2026 | [Sum Divisible By Three](../custom/arrays/sum_divisible_by_three.py) | 1h 20m | Basic DS, Iteration, Loops |
| Feb 15, 2026 | [Positive Negative Count](../custom/arrays/positive_negative_count.py) | ~40 mins | Control Flow, Conditionals |
| Feb 15, 2026 | [Even Odd Analysis](../custom/arrays/even_odd_analysis.py) | ~30 mins | Counting + Summing, Nested Conditionals, Decision Logic |
| Feb 16, 2026 | [Maximum Circular Subarray Sum](../custom/arrays/maximum_circular_subarray_sum.py) | ~3 hours (in progress) | Kadane’s Algorithm, Circular Arrays, Edge Cases |

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

### 5. Maximum Circular Subarray Sum (in progress)
**File:** `custom/arrays/maximum_circular_subarray_sum.py`
**Date:** February 16, 2026
**Time Spent:** ~3 hours (so far)

**Key Learnings / Findings so far:**
1. **Kadane’s algorithm is the core building block** for finding the max sum over any contiguous subarray.
2. **Circular trick idea** (still working through it):
    - Best circular sum often equals `total_sum - (minimum subarray sum)`.
3. **Important edge case**:
    - If all numbers are negative, the answer is the maximum (least negative) single element (and the circular trick can give 0, which would be wrong).

---

## Kadane’s Algorithm (Max Subarray Sum) — finding for Circular Subarray

This is a reference flowchart for the **standard (non-circular) Kadane’s algorithm** step that I’m using while working on the *Maximum Circular Subarray Sum* question.

```mermaid
flowchart TD
    A[Start] --> B[Initialize: 
        maxSoFar = -∞ 
        maxEndingHere = 0 
        start=0, end=0, s=0]

    B --> C[For each element arr[i]]
    C --> D[Add arr[i] to maxEndingHere]

    D --> E{Is maxEndingHere > maxSoFar?}
    E -->|Yes| F[Update maxSoFar = maxEndingHere
                 start = s, end = i]
    E -->|No| G[Do nothing]

    F --> H{Is maxEndingHere < 0?}
    G --> H

    H -->|Yes| I[Reset: 
                 maxEndingHere = 0 
                 s = i+1]
    H -->|No| J[Continue]

    I --> C
    J --> C

    C --> K[End of loop]
    K --> L[Result: 
             maxSoFar = maximum subarray sum 
             Subarray = arr[start...end]]

    %% Edge case notes
    L --> M[Edge Cases:
             • Full array if sum never < 0
             • Exclude elements if they weaken sum
             • All negatives → least negative element
             • Multiple equal sums → first chosen]
```
