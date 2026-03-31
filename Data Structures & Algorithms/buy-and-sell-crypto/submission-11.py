class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]

        for i in range(len(prices)):
            if i > 0 and prices[i] < prices[i-1]:
                minPrice = min(prices[i], minPrice)
            res = max(res,prices[i] - minPrice)
        return res 