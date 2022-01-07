from typing import List


def maxProduct(nums: List[int]) -> int:
    curMin, curMax = 1, 1
    result = max(nums)

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue
        temp = n * curMax
        curMax = max(n*curMax, n*curMin, n)
        curMin = min(temp, n*curMin, n)
        result = max(result, curMax, curMin)
    return result
