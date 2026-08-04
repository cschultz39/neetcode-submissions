class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map -> value to index
        # find if target - nums[i] is a value in list
        # use empty hashmap
        # add elements as we go, will find first val when check second val

        seenMap = {} # val : idx

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seenMap:
                return[seenMap[diff], i]
            seenMap[nums[i]] = i
        
        return