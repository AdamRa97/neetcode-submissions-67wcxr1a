class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(prices):
            res = max(res, prices[r] - prices[l])
            while prices[l] > prices[r]:
                l += 1
            r += 1
        return res