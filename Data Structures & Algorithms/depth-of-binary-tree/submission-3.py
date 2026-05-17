# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        depth = 0
        while stack:
            depth += 1  # Increment depth at each level
            next_level = []  # Track nodes at the next level
            
            for node in stack:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            stack = next_level  # Move to the next level
        
        return depth

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        