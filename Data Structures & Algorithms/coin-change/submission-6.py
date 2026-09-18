class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [math.inf]* (amount+1)
        # the dp is the number of coins we need to make this particular amount
        # dp[i] holds the min coins we need to make amount i
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                # just a check to make sure that we need not do computation for a useless coin
                if (i - coin)< 0:
                    break
                if (dp[i-coin]!= math.inf):
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount]== math.inf else dp[amount]



        