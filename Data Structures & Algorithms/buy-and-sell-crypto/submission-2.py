class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # build backwards, finding best day to buy based on sell

        # save max profit and curr profit
        # this solution was O(n^2) w nested loops

        # save max profit and max price so far

        max_profit = 0
        max_price = 0

        for price in reversed(prices):
            if price > max_price:
                max_price = price
            elif max_price - price > max_profit:
                max_profit = max_price - price
        
        return max_profit