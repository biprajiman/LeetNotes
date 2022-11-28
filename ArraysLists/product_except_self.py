from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    product_left = [1] * n
    product_right = [1] * n

    for i in range(1, n):
        product_left[i] = product_left[i-1] * nums[i - 1]
    
    for i in range(n-2, -1, -1):
        product_right[i] = product_right[i+1] * nums[i+1]
    
    answer = [1] * n
    for i in range(n):
        answer[i] = product_left[i] * product_right[i]
    
    return answer


if __name__ == '__main__':
    tests_pairs = [([1, 2, 3, 4], [24, 12, 8, 6]),
                    ([], []),
                    ([0, 1, 2, 3], [6, 0, 0, 0]),
                    ([0, 0, 3, 4], [0, 0, 0, 0]),
                    ([-1, -2, -3, -4], [-24, -12, -8, -6])]

    for (test, answer) in tests_pairs:
        result = product_except_self(test)
        assert  result == answer, result