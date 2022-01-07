# def solution(nums: int, k:int):
#     occur = { 0 : 1 }
#     counter = 0
#     curSum = 0

#     for i in range(len(nums)):
#         curSum += nums[i]
#         diff = curSum - k
#         if diff in occur:
#             counter += occur[diff]
#         if curSum in occur:
#             occur[diff] += 1
#         else:
#             occur[curSum] = 1
#     return counter

def solution(nums: int, k: int) -> int:
    counter = 0
    currSum = 0
    occur = {0: 1}

    for i in nums:
        currSum += i
        diff = currSum - k
        counter += occur.get(diff, 0)
        occur[currSum] = 1 + occur.get(currSum, 0)
    return counter
