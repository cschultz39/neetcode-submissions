class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # no duplicate triplets
        # no duplicate indices
        # three pointers, sort array?

        nums.sort()
        n = len(nums)
        output = []

        curr = 0
        while curr < n-2:
            l = curr + 1
            r = n - 1

            while l < r:
                curr_sum = nums[curr] + nums[l] + nums[r]

                if curr_sum == 0:
                    output.append([nums[curr], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr_sum < 0:
                    l += 1
                else: 
                    r -= 1
            
            curr += 1
            while curr < n - 2 and nums[curr] == nums[curr -1]:
                curr += 1
        
        return output