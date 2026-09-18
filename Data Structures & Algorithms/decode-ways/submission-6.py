class Solution:
    def numDecodings(self, s: str) -> int:
        # this is one type of dp where we have to check previous step along with two steps before, basically like climbing steps with possibilities of 1 and 2
        # the idea becomes at current step, what are the ways and the next step
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0]* (n+1)
        # base case
        # string is empty
        dp[0] = 1
        # only 1 character in string
        dp[1] = 1

        # dp[i] controls the most part, dp[i] holds 1st element info along with second element info, 
        # when checking second element, we are adding the count with 1st element info, only to preserve counts
        
        for i in range(2, n+1):
            # we first add the first digit, this has count till 1st digit
            if s[i-1] !='0':
                dp[i]+= dp[i-1]
            # after adding the first digit, we check the second digit till now, 
            # we updated the count with 1 digit before, we add second digit along with count till i-2
            two_digit = int(s[i-2:i])
            if 10<=two_digit<=26:
                dp[i]+= dp[i-2]
        return dp[n]
            

        
        
        