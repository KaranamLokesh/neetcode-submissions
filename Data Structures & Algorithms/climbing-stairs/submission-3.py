class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        # dp is all about the chances you have and the choices you make
        dp = [0]*n
        # base case 
        # when there is 1 step, you only have 1 choice
        dp[0] = 1
        # when there are 2 steps, you only have 2 choice, you can take 1+1 or 2
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
        