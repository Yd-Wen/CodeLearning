# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历
class Solution1(object):
  def isValidBST(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    res = []
    def inorder(node):
      if node:
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    inorder(root)
    if (len(res) != len(set(res))): return False
    sorted_res = sorted(res)
    if (tuple(res) == tuple(sorted_res)): return True
    else: return False


# 递归
class Solution2(object):
  def isValidBST(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    def helper(node, low=float('-inf'), high=float('inf')):
      if not node:
        return True
      if node.val <= low or node.val >= high:
        return False
      return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    return helper(root)
