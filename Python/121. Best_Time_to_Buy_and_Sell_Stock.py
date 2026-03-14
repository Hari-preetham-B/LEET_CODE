class Solution(object):
    def maxProfit(self, prices):
        profit=0
        min=prices[0];
        for i in prices:
            if min>i:
                min=i
            profit1=i-min
            if profit1>profit:
                profit=profit1
        return profit
