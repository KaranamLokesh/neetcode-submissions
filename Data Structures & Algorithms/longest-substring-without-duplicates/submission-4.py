class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        if len(s)==0 or len(s)==1:
            return len(s)

        substring = s[l]
        max_length = 0
        while r < len(s):
            if s[r] not in substring:
                substring+=s[r]
                length = r-l+1
                max_length = max(max_length, length)
                r+=1
            else:
                l+=1
                substring = substring[1:]
            
        return max_length
            





        