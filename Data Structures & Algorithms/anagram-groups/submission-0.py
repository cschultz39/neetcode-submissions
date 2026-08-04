class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hashmap
        # for each word, make array to count characters
        # use array as key, value is list of str with same count array

        countMap = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            countMap[tuple(count)].append(string)

        return list(countMap.values())
        