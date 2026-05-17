# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check_tree(self, p,q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.check_tree(p.left, q.left) and self.check_tree(p.right, q.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.check_tree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        



        