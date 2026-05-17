class Solution:
    def countSubstrings(self, s: str) -> int:
        # the idea is to start checking for palindromes by assuming curr character is the middle 
        # of the palindromic substring
        n = len(s)
        res = 0
        for i in range(n):
            l,r = i,i
            # this checks for odd length palindromes because it starts in the middle char with length 1 
            # and expands to left and right by 1, increasing the string length to 3
            while l>=0 and r <n and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
            # check the palindromes of even length
            l =i
            r = i+1
            # we start by checking palindromes of length = 2na d expand to left and right by 1, increasing length to 4
            while l>=0 and r<n and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            
        return res
            
        
        