# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max_dia = 0
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            
            # 计算直径
            self.max_dia = max(self.max_dia, left + right)
            # 返回当前节点的高度/深度
            return max(left, right) + 1
        
        height(root)
        return self.max_dia
