# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution1(object):
  def inorderTraversal(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    res = []
    def inorder(root):
      if root:
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    
    inorder(root)
    return res

# 迭代
class Solution2(object):
  def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result

# Morris
class Solution3(object):
  def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    current = root
    prev = current

    while current:
      if not current.left: 
        result.append(current.val)
        current = current.right
      else:
        prev = current.left
        while prev.right and prev.right != current: 
          prev = prev.right
        if prev.right == current:
          prev.right = None  # 恢复树
          result.append(current.val)
          current = current.right
        else:
          prev.right = current
          current = current.left

    return result


if __name__ == "__main__":
    s = Solution3()
    print(s.inorderTraversal([1,None,2,3]))

        