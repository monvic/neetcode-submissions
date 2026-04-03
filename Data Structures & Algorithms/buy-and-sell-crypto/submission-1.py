class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyI = 0
        sellI = 1
        profit = 0
        while sellI < len(prices):
            if prices[sellI] < prices[buyI]:
                buyI = sellI

            elif prices[sellI] > prices[buyI]:
                # print(prices[buyI], prices[sellI])
                profit = max(profit, prices[sellI] - prices[buyI])
            
            sellI += 1
        
        return profit
                

        