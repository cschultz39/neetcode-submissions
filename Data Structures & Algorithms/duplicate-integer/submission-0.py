class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use set for 0(1) lookup time
        # loop through array checking for matches
        # add element to set if no match

        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
        