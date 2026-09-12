class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # build backwards, finding best day to buy based on sell
        # save max profit and curr profit
        # dp so need array to keep values?

        n = len(prices)
        max_profit = 0

        for i in range(n-1, -1, -1):
            curr_sell = prices[i]
            curr_profit = 0
            for j in range(i):
                if curr_profit < curr_sell - prices[j]:
                    curr_profit = curr_sell - prices[j]
            if max_profit < curr_profit:
                max_profit = curr_profit
        
        return max_profit