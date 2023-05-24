class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stock = prices[0]
        for i in range(1, len(prices)):
            cur = prices[i]
            if cur > stock:
                profit += cur - stock
            stock = cur
        return profit