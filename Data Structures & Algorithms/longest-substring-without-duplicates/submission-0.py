class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash table, sliding window
        # something with quick lookup to save seen characters
        # save running length and left+right chars

        curr_len = 0
        max_len = 0
        chars = set()
        left = 0

        for right in range(len(s)):
            char = s[right]

            while char in chars:
                chars.remove(s[left])
                left += 1
                curr_len -= 1

            chars.add(char)
            curr_len += 1

            if curr_len > max_len:
                max_len = curr_len
        
        return max_len