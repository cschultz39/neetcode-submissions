class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find product of entire array, divide by each value
        # doesnt work with 0 

        # left and right of current place, multiply those together
        # two passes
        
        n = len(nums)
        output = [1]*n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
