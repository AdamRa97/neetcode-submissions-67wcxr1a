from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqMap1 = [0] * 26

        for i in range(len(s)):
            idx1 = ord('a') - ord(s[i])
            idx2 = ord('a') - ord(t[i])
            freqMap1[idx1] += 1
            freqMap1[idx2] -= 1
        
        for freq in freqMap1:
            if freq != 0:
                return False
        return True