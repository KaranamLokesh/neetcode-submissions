class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        # there are 3 conditions we need to follow
        # 1. open < n
        # 2. add closing paranthesis only when number of open > number of close
        # 3. valid when open == closed == n
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

            if openN > closedN:
                stack.append(")")
                backtrack(openN, closedN+1)
                # as we are backtracking we want to remove the current state else, we will redo the same one again and get TLE
                stack.pop()
        # start the process
        backtrack(0,0)
        return res

            
        