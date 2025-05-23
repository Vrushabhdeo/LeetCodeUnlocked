"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) in [0, 1]:
        #     return 0
        # elif len(prices) == 2:
        #     if prices[1] > prices[0]:
        #         return prices[1] - prices[0]
        #     return 0
        # elif len(prices) > 2:
        #     buy_price = min(prices)
        #     buy_date = prices.index(buy_price)
        #     sell_price = max(prices)
        #     sell_date = prices.index(sell_price)
        #     if sell_date > buy_date:
        #         return sell_price - buy_price
        #     else:
        #         max_profit = 0
        #         for i in range(len(prices)-1):
        #             for j in range(i+1, len(prices)):
        #                 if prices[i] < prices[j]:
        #                     max_profit = max(max_profit, prices[j]-prices[i])
        #         return max_profit
        if len(prices) < 2:
            return 0

        max_profit = 0
        current_profit = 0

        for i in range(1, len(prices)):
            # Price difference between today and yesterday
            price_diff = prices[i] - prices[i - 1]
            # Kadane's logic: reset or accumulate
            current_profit = max(price_diff, current_profit + price_diff)
            # Track the global maximum
            max_profit = max(max_profit, current_profit)

        return max_profit if max_profit > 0 else 0
