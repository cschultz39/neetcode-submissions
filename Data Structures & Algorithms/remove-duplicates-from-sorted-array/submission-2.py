class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers
        # one stays at place to compare
        # other moves forward, moves next unique value to the next spot
        # both move forward 1 
        # stop when other hits end
        # keep count

        stay = 0
        search = None

        for i in range(1, len(nums)):
            search = i

            if nums[stay] != nums[search]:
                if search > stay + 1:
                    nums[stay + 1] = nums[search]
                stay += 1

        return stay + 1        