# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def whetherSym(l, r):
            if l == None and r == None:
                return True
            if l and r and l.val == r.val:
                return whetherSym(l.left, r.right) and whetherSym(l.right, r.left)
            else:
                return False

        return whetherSym(root.left, root.right) 
        