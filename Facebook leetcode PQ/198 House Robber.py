# from typing import List


# def rob(self, nums: List[int]) -> int:
#     rob1, rob2 = 0, 0

#     # [rob1, rob2, n, n+1, ...]
#     # updating to the next house,
#     #       [rob1, rob2, n, n+1, ...]
#     #              [rob1, rob2, n, n+1, ...]
#     #                     [rob1, rob2, n, n+1, ...]... DR(recursion approach)
#     # Therefore, I can just put rob2 = temp
#     for n in nums:
#         temp = max(rob1 + n, rob2)
#         rob1 = rob2
#         rob2 = temp
#     return rob2

# DP (bottom-up approach) 
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        #special handling for special case.
        if not nums:
            return 0
        
        # maxRobbedAmount = [None for i, num in enumerate((nums) + 1)]
        maxRobbedAmount = [None for _ in range(len(nums)-1)]
        N = len(nums)

        #base case initialization
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        #DP table calculations.
        for i in range(N - 2, -1, -1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
        return maxRobbedAmount[0]