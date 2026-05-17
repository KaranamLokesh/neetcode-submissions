class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            d[s[i]]=1+d.get(s[i],0)
            d[t[i]]=d.get(t[i],0) -1
        for val in d:
            print(d)
            if d[val]!=0:
                return False

        return True

        