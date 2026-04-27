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

    # 前序遍历：根 → 左 → 右
    def preorderTraversal(self, root):
            result = []
            stack = []
            current = root

            while current or stack:
                    while current:
                            result.append(current.val)  # 一遇到就访问（根）
                            stack.append(current)
                            current = current.left
          
                    current = stack.pop()
                    current = current.right         # 不再访问，直接去右

            return result

    # 后序遍历：左 → 右 → 根
    def postorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
                while current:
                        result.append(current.val)  # 先访问根
                        stack.append(current)
                        current = current.right      # 先往右！

                current = stack.pop()
                current = current.left           # 再往左！

        return result[::-1]  # 最后反转！


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
            # 无左往右走
            if not current.left: 
                result.append(current.val)
                current = current.right
            # 有左找前驱
            else:
                # 找到前驱
                prev = current.left
                while prev.right and prev.right != current: 
                    prev = prev.right
                # 前驱有右指当前，往右走
                if prev.right == current:
                    prev.right = None  # 恢复树
                    result.append(current.val)
                    current = current.right
                # 前驱无右置为空，往左走
                else:
                    prev.right = current
                    current = current.left

        return result


if __name__ == "__main__":
        s = Solution3()
        print(s.inorderTraversal([1,None,2,3]))

        