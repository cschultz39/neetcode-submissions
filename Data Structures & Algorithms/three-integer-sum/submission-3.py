class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # no duplicate triplets
        # sort and fix 1, 2 pointer the rest

        # sort the array
        # loop i from 0 to n-2, fixing one number
        # skip duplicates

        nums.sort()
        n = len(nums)
        output = []

        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif cur < 0:
                    left += 1
                else:
                    right -= 1
        
        return output