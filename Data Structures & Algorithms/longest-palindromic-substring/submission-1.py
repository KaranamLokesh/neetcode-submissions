class Solution:
    def is_pal(self, s):
        return s == s[::-1]
    def longestPalindrome(self, s: str) -> str:
        st = ""
        n =len(s)
        dp = [False]*(n+1)
        dp[0] = True
        maxi = 0
        for i in range(1,n+1):
            for j in range(i):
                if self.is_pal(s[j:i]):
                    
                    if len(s[j:i])> maxi:
                        st = s[j:i]
                        maxi = len(s[j:i])
        return st


        