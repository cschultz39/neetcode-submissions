class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        j = 0
        k = n-1

        while j < k:
            while j < n and not s[j].isalnum():
                j += 1
            while -1 < k and not s[k].isalnum():
                k -= 1
            if j < k and s[j].lower() != s[k].lower():
                return False
            j += 1
            k -= 1
        
        return True
        