class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # move right until see repeat, then move left
        # track chars in set (update when window shrinks)
        # track max len
        
        n = len(s)
        seen = set()
        max_len = 0

        l = 0
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_len = max(max_len, r-l+1)
        
        return max_len
                