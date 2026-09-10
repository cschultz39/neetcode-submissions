class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # uppercase letters
        # choose k chars to replace
        # make longest possible substring of same chars
        # hash table, sliding window
        
        # sliding window that increases until k chars need to be replaced to be continuous, save length
        # get rid of leftmost char and do same process, tracking longest
        # how to distinguish between repeating continuous chars and repeated separate chars?

        # need a dict to keep count
        # valid window is when (right - left + 1) - max repeated chars <= k
        # move right until window is invalid, then move left to make window valid again

        char_count = dict()
        max_window = 0
        max_rep_char = 0
        left = 0

        for right in range(len(s)):
            # add/update char in dictionary
            char_count.update({s[right] : char_count.get(s[right], 0) + 1})
            if char_count.get(s[right]) > max_rep_char:
                max_rep_char = char_count.get(s[right])
            
            # check validity of window
            if (right - left + 1) - max_rep_char <= k:
                if max_window < (right - left + 1):
                    max_window = right - left + 1
            else:
                char_count.update({s[left] : char_count.get(s[left]) - 1})
                left += 1
        
        return max_window
