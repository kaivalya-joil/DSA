class Solution(object):
    def maxProfit(self, prices):
        
        
        profit = 0
        buy = 0

        for i in range(len(prices) - 1):

            if prices[i] < prices[i + 1] and buy != 1:
                profit -= prices[i]
                buy = 1

            elif buy == 1:                    
                if prices[i+1] >= prices[i]:
                    pass                   
                else:
                    profit += prices[i]     
                    buy = 0

            

        
        if buy == 1:
            profit += prices[-1]

        return profit
                



        