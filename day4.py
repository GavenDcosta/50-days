#Leet Code

#Buy Two Chocolates

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if(prices[0] + prices[1] > money):
            return money
        else:
            remaining = money - prices[0] - prices[1]
            return remaining    