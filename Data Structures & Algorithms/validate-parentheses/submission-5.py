class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        stack = []
        for char in s:
            print(stack)
            if char == "(" or char == "[" or char == "{":
                count+=1
                stack.append(char)
            if char == ")":
                if stack and stack[-1] == "(":
                    count-=1
                    stack.pop()
                    
                else:
                    return False
            elif char == "]":
                if stack and stack[-1] == "[":
                    count-=1
                    stack.pop()
                   
                else:
                    return False
            elif char == "}":
                if stack and stack[-1] == "{":
                    count-=1
                    stack.pop()
                    
                else:
                    return False

            
        return count == 0
                
        