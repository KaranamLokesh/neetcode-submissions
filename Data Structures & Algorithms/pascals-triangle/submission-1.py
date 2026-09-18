class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        dp = [[1]]*numRows
        for i in range(1,numRows):
            dp[i] = (i+1)* [1]
        if numRows >1:
            dp[1] = [1,1]
        for i in range(2,numRows):
            dp[i][0] = 1
            for j in range(1,len(dp[i-1])):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dp
        