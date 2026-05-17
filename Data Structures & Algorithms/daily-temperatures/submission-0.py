class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]* len(temperatures)
        stack = []
        
        i = 0
        # for i,t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         stackT, stackInd = stack.pop()
        #         result[stackInd] = i - stackInd
        #     stack.append((t,i))

        while i < len(temperatures):

            while stack and stack[-1][0] < temperatures[i]:
                # result[i] = i - stack[-1][1]
                # stack.pop()
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((temperatures[i], i))
            print(stack)
            i+=1
            
        return result




        