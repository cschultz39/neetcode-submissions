class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # valid substring = window len - rep chars <= k
        # sliding window with l and r
        # build up until invalid window, then move l over until valid again
        # track max window, curr longest rep chars

        n = len(s)
        rep_count = 0
        chars = dict()
        max_len = 0

        left = 0
        for right in range(n):
            chars.update({s[right]: chars.get(s[right], 0) + 1})
            rep_count = max(rep_count, chars[s[right]])

            if (right-left+1) - rep_count <= k:
                max_len = max(max_len, right-left+1)
            else:
                if chars[s[left]] <= 1:
                    del chars[s[left]]
                else: 
                    chars.update({s[left]: chars[s[left]] - 1})
                left += 1
        
        return max_len
