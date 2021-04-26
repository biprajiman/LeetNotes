# Description
Problems in this category can be solved with or some modified version of binary search.

# General Notes:
- Applicable to lists or arrays and matrix
- Time complexity O(logN) -> N = total number of elements
- Needs to be sorted in some way

# Problem Note:
- Find minimum in rotated array ([Leetcode Problem 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/))
    - Loop while left pointer is smaller than right pointer.
    - Find rotation point. Check mid with end.
    - If mid is smaller than right, min is on the left half. Move the right pointer to mid.
    - Else potential rotation and move left pointer to mid + 1. 
    - At the end right pointer will be the minimum value.
- 