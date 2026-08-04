class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # each element is product of everything to left * everything to right
        # prefix and suffix
        # build output in two passes with running product

        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
        