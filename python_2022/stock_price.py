class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell_value = max(prices)
        test_price = []
        if prices is [] or len(prices) == 1:
            return 0
        for price in prices:
            test_price.append(abs(price - sell_value))
        profit_index = test_price.index(max(test_price))
        sell_index = prices.index(sell_value)
        if profit_index > sell_index:
            index_of_o = test_price.index(0)
            prices.pop(index_of_o)
        else:
            return test_price[profit_index]
        final_price = self.maxProfit(prices)
        return final_price

    def maxProfit(self, prices):
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]  # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit

sol = Solution()
print(sol.maxProfit([2,4,1]))
print(sol.maxProfit([7,1,5,3,6,4]))