class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        charDict = defaultdict(int)

        for r in range(len(s)):
            charDict[s[r]] += 1
            while (r -l + 1) - max(charDict.values()) > k:
                charDict[s[l]] -= 1
                l += 1 
            res = max(res, (r-l) + 1)
        return res