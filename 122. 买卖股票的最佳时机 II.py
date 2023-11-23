class Solution(object):
    def maxProfit(self, prices):
        profix = []
        _sum = [0]
        for idx in range(1,len(prices)):
            profix.append(prices[idx] - prices[idx-1])
            _sum.append(_sum[-1] + profix[idx-1])
        money = 0
        for p in profix:
            if p > 0:
                money += p
        return money