class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the strings so letters are in general order
        # compare sorted strings

        s_sort = sorted(s)
        t_sort = sorted(t)

        return s_sort == t_sort
        