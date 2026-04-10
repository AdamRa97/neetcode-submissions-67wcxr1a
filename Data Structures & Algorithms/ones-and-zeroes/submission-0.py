class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def dfs(i, zero, one):
            if i == len(strs):
                return 0
            if (i, zero, one) in memo:
                return memo[i,zero,one]

            zeroLimit = strs[i].count("0")
            oneLimit = len(strs[i]) - zeroLimit
            
            skip = dfs(i+1, zero, one)

            take = 0
            if zero >= zeroLimit and one >= oneLimit:
                take = 1 + dfs(i+1, zero - zeroLimit, one - oneLimit)

            res = max(skip, take)
            memo[i,zero,one] = res
            return res
            
        return dfs(0,m,n)