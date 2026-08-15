class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # negative = restart
        # choose to continue current sum or start over
        # replace max sum if greater

        n = len(nums)
        curr_max = nums[0]
        global_max = nums[0]
        
        for i in range(1, n):
            if curr_max < 0:
                curr_max = nums[i]
            else:
                curr_max += nums[i]
            global_max = max(global_max, curr_max)
        
        return global_max