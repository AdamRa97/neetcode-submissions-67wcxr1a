from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freqMap1 = [0] * 26
        freqMap2 = [0] * 26

        for i in range(len(s)):
            idx1 = ord('a') - ord(s[i])
            idx2 = ord('a') - ord(t[i])
            freqMap1[idx1] += 1
            freqMap2[idx2] += 1
        
        if freqMap1 != freqMap2:
            return False
        return True