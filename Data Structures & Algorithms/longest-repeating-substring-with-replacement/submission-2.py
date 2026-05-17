class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l=0
        max_count = 0
        max_result = 0
        for r in range(len(s)):
            counts[s[r]]=1+counts.get(s[r],0)
            max_count = max(max_count, counts[s[r]])
            while(r-l+1) - max_count >k:
                counts[s[l]]-=1
                l+=1
            max_result = max(max_result, r-l+1)
        return max_result
            


        