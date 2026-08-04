class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make all lowercase lower()
        # only letters and numbers, remove everything else isalnum()
        # compare with two pointers

        s_lower = s.lower()
        i = 0
        j = len(s) - 1

        while i < j:
            while i < len(s) and not s_lower[i].isalnum():
                i += 1
            while j > -1 and not s_lower[j].isalnum():
                j -= 1
            if i < j and s_lower[i] != s_lower[j]:
                return False
            i += 1
            j -= 1
        
        return True
