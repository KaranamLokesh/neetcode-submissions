class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair of elements, index and height
        for i,h in enumerate(heights):
            start = i
            ## the idea is we loop the stack to check if the current value is greater
            ## than the top element in stack, then we pop the element from the stack, 
            ## calculate area, and put the start index of the current element as that index from stack,
            ## and add that index to the current element
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (i - index)* height)
                start = index
            stack.append((start, h))

        ## when you get to the end, the stack is not empty, we have to calculate 
        for i,h in (stack):
            max_area = max(max_area, (len(heights) - i)* h)

        return max_area

        



        