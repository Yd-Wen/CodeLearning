# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前序遍历：递归
class Solution1(object):
  def flatten(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: None Do not return anything, modify root in-place instead.
    """
    res = []
    def preorder(node):
      if node:
        res.append(node)
        preorder(node.left)
        preorder(node.right)
    preorder(root)

    for i in range(len(res)-1):
      prev, curr = res[i], res[i+1]
      prev.left = None
      prev.right = curr
        

# 前序遍历：迭代
class Solution2(object):
  def flatten(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: None Do not return anything, modify root in-place instead.
    """
    res = []
    stack = []
    
    while stack or root:
      while root:
        res.append(root)
        stack.append(root)  # stack 不能省，用于迭代
        root = root.left
      root = stack.pop()
      root = root.right
    
    for i in range(len(res)-1):
      prev, curr = res[i], res[i+1]
      prev.left = None
      prev.right = curr


# 前序遍历（迭代）和展开同步进行
class Solution3(object):
  def flatten(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: None Do not return anything, modify root in-place instead.
    """
    if not root: return
    stack = [root]
    prev = None

    while stack:
      curr = stack.pop()
      if prev:
        prev.left = None
        prev.right = curr
      if curr.right: stack.append(curr.right)
      if curr.left: stack.append(curr.left)
      prev = curr


# 寻找前驱节点
class Solution4(object):
  def flatten(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: None Do not return anything, modify root in-place instead.
    """
    curr = root
    while curr:
      if curr.left:
        prev = curr.left
        while prev.right:
          prev = prev.right
        prev.right = curr.right
        curr.right = curr.left
        curr.left = None
      curr = curr.right
