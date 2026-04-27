# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        def level(nodes):
            if not nodes: return
            r = []
            new_nodes = []
            for node in nodes:
                if not node: continue
                r.append(node.val)
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            if len(r): res.append(r)
            level(new_nodes)
        level([root])
        return res  
    