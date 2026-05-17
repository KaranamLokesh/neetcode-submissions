class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp= [0]*(n)
        min_dp = [0]*n
        max_dp[0] = min_dp[0] = nums[0]
        maxi = nums[0]
        # the idea is to keep track of 3 things
        # 1. is the current element the start of the new sub array
        # 2. is the current number * max till now still positive
        # 3. is the current number * min till noe becomes positive
        # 3. Always Consider Three Possibilities at Each Step
        # At each position, the maximum or minimum product subarray ending at that position is either:

        # The current number itself (start new subarray)

        # The current number times the previous max

        # The current number times the previous min
        for i in range(1,n):
            max_dp[i] = max(nums[i], nums[i]* max_dp[i-1], nums[i]* min_dp[i-1])
            min_dp[i] = min(nums[i], nums[i]* max_dp[i-1], nums[i]* min_dp[i-1])
            maxi = max(maxi, max_dp[i])
        return maxi
        