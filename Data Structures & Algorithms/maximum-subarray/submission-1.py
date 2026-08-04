class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # greedy approach, max sum check
        # either extend or start over

        n = len(nums)
        if n == 1:
            return nums[0]

        curSum = 0
        maxSum = nums[0]

        for i in range(n):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSum = curSum if curSum > maxSum else maxSum

        return maxSum