class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        l, r = 0, len(s)-1

        while l < r:
            while not isAlphaNum(s[l]) and l < r:
                l += 1
            while not isAlphaNum(s[r]) and r > l:
                r -= 1
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True