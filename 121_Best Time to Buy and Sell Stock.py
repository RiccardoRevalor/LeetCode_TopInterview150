class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        max = -99
        l = len(prices)
        for i in range(l):
            for j in range(i+1, l):
                diff = prices[j] - prices[i]
                if (diff > max): 
                    max = diff
        if max < 0: return 0
        return max        
    
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price: min_price = p
            if p - min_price > max_profit: max_profit = p - min_price

        return max_profit

