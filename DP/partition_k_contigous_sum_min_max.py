"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

E.g [1, 1, 2, 3] k =2

# need to try these different sums and get the largest sum
# minimize the largest sums
[1] [1, 2, 3] = largest sum (6)
[1, 1] [2, 3] = larget sum(5)
[1, 1, 2] [3] = largest sum(4)
minimize largest sum ([6, 5, 4]) = 4

[1,1,2,3]
[1] [1] [2, 3] = 5
[1] [1, 2] [3] = 3
[1, 1] [2] [3] = 3
"""

from functools import lru_cache
from typing import List


def minimize_largest_sum(nums: List[int], k: int) -> float:
    n = len(nums)
    
    @lru_cache()
    def dp(i, m):
        if i == n:
            if m == 0:
                return 0
            else:
                return float('inf')
        
        if m == 0:
            return float('inf')
        
        curr_sum = 0
        ans = float('inf')

        for j in range(i, n):
            curr_sum += nums[j]
            ans = min(ans, max(curr_sum, dp(j + 1, m - 1)))
        
        return ans

    return dp(0, k)


if __name__ == '__main__':
    nums = [1, 1, 2, 3]

    result = minimize_largest_sum(nums, k=2)
    assert result == 4, nums

    result = minimize_largest_sum(nums, k=3)
    assert result == 3, nums

    nums = [7,2,5,10,8]
    k = 2
    result = minimize_largest_sum(nums, k=k)
    assert result == 18

    k = 6
    result = minimize_largest_sum(nums, k=k)
    assert result == float('inf')