# Description:
Problems related to arrays and lists. These problems may have some tricks to solve and do not belong to other categories.

# Problem Notes:
1. Find the smallest missing positive integer in unsorted array nums of integers[Leetcode Problem 41](https://leetcode.com/problems/first-missing-positive/)
    - First thing to remember, list could potentially contain negative integers.
    - Idea here is to consider number as index of array and flip the values at the index from positive to negative. If number is missing value at index will be positive after the flip.
    - First change all the numbers greater than len(nums) and less than or equal to 0 to some large positive value.
    - Go through each element and if it is within index [0, len(nums)) flip the value to negative. Remember to use abs(ele) here since numbers could be negated before. Edge case example -1, 1. Try it out.
    - At the end go through the array if number is flipped then number is there, if not number is missing.
2. Find missing number in array nums containing n distinct numbers in the range of [0, n].
    - Only difference here from problem 1 is that nums here contains only positive values.
    - Sum actual and expected.
    - Get the difference.
    - Could potentially be solved with above idea. 