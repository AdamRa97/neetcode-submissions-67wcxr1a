from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMapS = Counter(s)
        freqMapT = Counter(t)

        return freqMapS == freqMapT