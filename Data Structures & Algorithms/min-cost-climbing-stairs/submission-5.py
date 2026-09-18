class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # this is almost same as climbing stairs possibilities, but comes with a cost
        stairs = len(cost)
        if stairs == 1:
            return cost[0]
        
        dp = [0]* (stairs+1)
        # the logic is you can go i+1 step or i+2 step forwards with cost from ith step
        # base case
        # if there are only 1 steps, cost is nothing as we can choose to start at 0
        dp[0] = 0
        # if there are 2 steps, cost is nothing as we can choose to start at 1
        dp[1] = 0
        for i in range(2, stairs+1):
            # the logic is we will take the current step with cost[i] and the minimum cost we were able to reach to current point
            dp[i] =  min(dp[i-1]+ cost[i-1], cost[i-2]+dp[i-2]) 
        return dp[stairs]

        