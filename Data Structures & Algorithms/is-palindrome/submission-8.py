class Solution:
    def isPalindrome(self, s: str) -> bool:
        # one left ptr and one right ptr
        # move both until both are at alphanum chars
        # compare
        
        # how to make sure no overlap when moving?

        l, r = 0, len(s)-1

        while l < r:
            while not s[l].isalnum() and l<r:
                l += 1
            while not s[r].isalnum() and l<r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1

        return True