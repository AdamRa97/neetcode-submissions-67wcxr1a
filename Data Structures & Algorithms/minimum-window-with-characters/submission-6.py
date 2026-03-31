from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        tCount = Counter(t)
        sCount = defaultdict(int)
        haveUnique = 0
        needUnique = len(set(t))
        for r in range(len(s)):
            sCount[s[r]] += 1
            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                haveUnique += 1
            while haveUnique == needUnique:
                if not res or len(res) > (r-l) + 1:
                    res = s[l:r+1]

                sCount[s[l]] -= 1
                if s[l] in tCount and tCount[s[l]] -1 == sCount[s[l]]:
                    haveUnique -= 1
                l += 1
        return res
            
