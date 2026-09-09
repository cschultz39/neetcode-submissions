class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # search + override

        n = len(nums)
        k = 1

        stay = 0
        search = 1
        while search < n:
            while search < n and nums[stay] == nums[search]:
                search+=1
            if search < n:
                nums[stay+1]=nums[search]
                stay+=1
                search+=1
                k+=1
        return k