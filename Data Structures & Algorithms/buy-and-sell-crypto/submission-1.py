class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # build backwards, finding best day to buy based on sell

        # save max profit and curr profit
        # this solution was O(n^2) w nested loops

        # save max profit and max price so far

        max_profit = 0
        max_price = 0

        for i in range(len(prices)-1, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            elif max_price - prices[i] > max_profit:
                max_profit = max_price - prices[i]
        
        return max_profit