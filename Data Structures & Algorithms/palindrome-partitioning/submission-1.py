class Solution:
    def palindrome(self, s, start, end):
        while (start<=end and s[start] == s[end]):
            start+=1
            end-=1
        if start > end:
            return True
        return False

    def pal_helper(self, s, startIndex, temp, res):
        n = len(s)
        ## base case
        if startIndex == n:
            res.append(temp.copy())
            return

        ## recursive case
        ## check if the substring from 
        for i in range(startIndex, n):
            if self.palindrome(s, startIndex, i):
                temp.append(s[startIndex:i+1])
                self.pal_helper(s, i+1, temp, res)
                temp.pop()

    def partition(self, s: str) -> List[List[str]]:
        temp = []
        res = []
        self.pal_helper(s, 0 ,temp, res)
        return res
        