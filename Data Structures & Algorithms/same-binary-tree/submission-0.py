# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_same(self, p,q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.check_same(p.left, q.left) and self.check_same(p.right, q.right)
        else:
            return False    
        

        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check_same(p,q)
            


        