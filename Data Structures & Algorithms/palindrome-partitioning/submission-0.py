class Solution:
    def palindrome(self, s, start, end):
        while (start<=end and s[start] == s[end]):
            start+=1
            end-=1
        if start > end:
            return True
        return False

    def pal_helper(self, s, index, temp, res):
        n = len(s)
        ## base case
        if index == n:
            res.append(temp.copy())
            return

        ## recursive case
        for i in range(index, n):
            if self.palindrome(s, index, i):
                temp.append(s[index:i+1])
                self.pal_helper(s, i+1, temp, res)
                temp.pop()

    def partition(self, s: str) -> List[List[str]]:
        temp = []
        res = []
        self.pal_helper(s, 0 ,temp, res)
        return res
        