class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)<2):
            return 0
        buy,sell=0,1
        maxProfit=0
        while(sell<len(prices) and buy<sell):
            if(prices[buy]<prices[sell]):
                temp=prices[sell]-prices[buy]
                maxProfit=max(maxProfit,temp)
            else:
                buy=sell
            sell+=1
        return maxProfit
        