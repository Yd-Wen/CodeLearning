# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 层序遍历
class Solution1(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        def helper(nodes):
            if not nodes: return
            new_nodes = []
            for node in reversed(nodes):
                if node:
                    res.append(node.val)
                    break
            for node in nodes:
                if node and node.left: new_nodes.append(node.left)
                if node and node.right: new_nodes.append(node.right)
            helper(new_nodes)
        helper([root])
        return res


# 根右左递归 + 记录深度
class Solution1(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        def helper(node, depth=0):
            if node:
                if depth == len(res):
                    res.append(node.val)
                helper(node.right, depth + 1)
                helper(node.left, depth + 1)
        helper(root)
        return res
