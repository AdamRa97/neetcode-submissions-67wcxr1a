from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap1 = Counter(s)
        freqMap2 = Counter(t)

        if freqMap1 != freqMap2:
            return False
        return True