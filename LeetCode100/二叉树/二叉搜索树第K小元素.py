# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历
class Solution1(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        res = []
        def inorder(node):
                if node:
                        inorder(node.left)
                        res.append(node.val)
                        inorder(node.right)
        inorder(root)
        return res[k-1]


# 迭代
class Solution(object):
        def kthSmallest(self, root, k):
                """
                :type root: Optional[TreeNode]
                :type k: int
                :rtype: int
                """
                stack = []
                while stack or root:
                        while root:
                                stack.append(root)
                                root = root.left
                        root = stack.pop()
                        k -= 1
                        if k == 0:
                                return root.val
                        root = root.right
        