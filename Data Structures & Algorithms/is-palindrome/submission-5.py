class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer
        # one at each end
        # need to ignore spaces, non alphanumeric chars
        
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)

        for i in range(n//2):
            front = s[i]
            back = s[n-i-1]
            if front != back:
                return False
        
        return True
