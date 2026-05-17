class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_count, s2_count = [0]*26, [0]*26
        ## Adding the counts of each char to an array
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]+=1
            s2_count[ord(s2[i])-ord('a')]+=1
        matches = 0
        l=0
        ## count all the positions in both the arrays where the count of chars is equal
        for i in range(26):
            matches+=(1 if s1_count[i]==s2_count[i]  else 0)
            
            ## As we have already added the elements till len of s1 above, no need to add them again, so we start from s1
        for r in range(len(s1), len(s2)):

            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2_count[index]+=1
            ## after adding the current char to array, if the counts of that char matched then add it to matches
            if s1_count[index] == s2_count[index]:
                matches+=1
                ## after adding if the count of curr char in s2 is a new one or exceeds the count of already existing count of char, 
                #then matches count decreases
            elif s1_count[index]+1 == s2_count[index]:
                matches-=1
            ## do the same thing for the left side, when we add a new element,
            ## we have to remove the previous element, as we are only taking a wndow size of len(s1) at a time
            index = ord(s2[l])- ord('a')
            ## as we are removing the element count decreases
            s2_count[index]-=1
            ## if after removing the char from array, if the char count at this index matches
            if s1_count[index] == s2_count[index]:
                matches+=1
                ## if after decrementing the count of current char, 
                ## if the count of char in s1 goes below existing count in s2
            elif s1_count[index] - 1 == s2_count[index]:
                matches-=1
            l+=1
        return matches == 26

        



        # count = 0
        # newstr = s1
        # for char in s2:
        #     if char in newstr:
        #         count+=1
        #         newstr = newstr.replace(char, "")
        #         print(newstr)
        #         if count == len(s1):
        #             return True
        # return False
                
            

        