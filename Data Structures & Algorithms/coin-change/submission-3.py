class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >=0:
                    dp[i] = min(dp[i], 1+ dp[i-coin])
        return dp[amount] if dp[amount]!= float('inf') else -1


    # def coin_change_helper(self, coins, temp, res, index, target):
    #     # base case
    #     if target == 0:
    #         res.append(len(temp))
    #         return
    #     elif target < 0:
    #         return
    #     # recursive case
    #     # iterate for each coin till the target is found
    #     # the idea is we start with index as 0, then go on till target is ==0 or <0, if <0, that means it has to
    #     # use a different number, go it comes back to the caller of this function and goes to next index
    #     for i in range(index, len(coins)):
    #         temp.append(coins[i])
    #         self.coin_change_helper(coins, temp, res, i, target-coins[i])
    #         temp.pop()

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     coins.sort(reverse=True)
    #     res = []
    #     self.coin_change_helper(coins, [], res, 0, amount)
    #     return min(res) if res else -1
        