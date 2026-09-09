class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # negative thing
        # current max and global max
        
        n = len(nums)
        curr_max = nums[0]
        global_max = nums[0]

        for i in range(1, n):
            curr_max = nums[i] if curr_max < 0 else curr_max + nums[i]
            global_max = curr_max if curr_max > global_max else global_max
        
        return global_max