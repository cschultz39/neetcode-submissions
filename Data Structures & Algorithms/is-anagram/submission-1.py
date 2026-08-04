class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check for diff lengths (cannot be anagrams)
        # sort the strings so letters are in general order
        # compare sorted strings

        if len(s) != len(t):
            return False

        s_sort = sorted(s)
        t_sort = sorted(t)

        return s_sort == t_sort
        