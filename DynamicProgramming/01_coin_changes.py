"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""


from typing import List

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # max_amount_from_coin = {}
#         #
#         # for coin in coins:
#         #     required_coins = int(amount / coin)
#         #     max_amount_from_coin[coin] = required_coins
#         #
#         # max_coins_required = -1
#         # for _ in sorted(max_amount_from_coin.keys(), reverse= True):
#         coins.sort(reverse=True)
#         print(coins)
#         coins_required = 0
#         curr_amount = 0
#         for i in range(len(coins)):
#             print("processing: {}".format(coins[i]))
#             if curr_amount != 0:
#                 coins_processed = int((amount - curr_amount) / coins[i])
#                 curr_amount += (coins[i] * coins_processed)
#                 print(coins_processed)
#                 print(curr_amount)
#                 coins_required += coins_processed
#             else:
#                 coins_processed = int(amount / coins[i])
#                 curr_amount = coins[i] * coins_processed
#                 print(coins_processed)
#                 print(curr_amount)
#                 coins_required += coins_processed
#         if curr_amount != amount:
#             return -1
#         print(coins_required)
#         return coins_required

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        print(dp)
        dp[0] = 0

        for coin in coins:
            print('Processing {}'.format(coin))
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
            print(dp)

        return dp[amount] if dp[amount] != float('inf') else -1

solution = Solution()
print(solution.coinChange([1,2,5], amount=11))