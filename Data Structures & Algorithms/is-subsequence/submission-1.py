class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i = 0
        j = 0
        if t == "":
            return False
        if s == "":
            return True
        while m:
            if j == len(t) -1 and m > 1:
                return False
            if s[i] == t[j]:
                i+=1
                j+=1
                m-=1
            else:
                j+=1
        return True
        