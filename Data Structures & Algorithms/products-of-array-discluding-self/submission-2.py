class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix with running product

        n = len(nums)
        output = n * [1]
        
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output