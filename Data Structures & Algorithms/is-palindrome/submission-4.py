class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        s=s.lower()
        for i in s:
            if (ord(i)>96 and ord(i)<123) or (ord(i)>= ord('0') and ord(i)<= ord('9')):
                st+=i
        l=0
        r = len(st)-1
        while l<=r:
            if(st[l]!=st[r]):
                return False
            l+=1
            r-=1
        return True


        
        