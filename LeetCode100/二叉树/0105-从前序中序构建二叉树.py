# Definition for a binary tree node.
class TreeNode(object):
        def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right


class Solution:
        def buildTree(self, preorder, inorder):
                index = {ele: i for i, ele in enumerate(inorder)}
                def helper(pre_left_idx, pre_right_idx, in_left_idx, in_right_idx):
                        if pre_left_idx > pre_right_idx: return None
                        pre_root_idx = pre_left_idx # 前序序列第一个是根节点
                        in_root_idx = index[preorder[pre_root_idx]]  # 中序序列中的索引
                        root = TreeNode(preorder[pre_root_idx])  # 建立根节点
            
                        size = in_root_idx - in_left_idx  # 左子树大小

                        root.left = helper(pre_left_idx + 1, pre_left_idx + size, 
                                                            in_left_idx, in_root_idx-1)
                        root.right = helper(pre_left_idx + size + 1, pre_right_idx, 
                                                            in_root_idx + 1, in_right_idx)
                        return root
        
                return helper(0, len(preorder)-1, 0, len(preorder)-1)


# 后序 + 中序 
class Solution:
    def buildTree(self, inorder, postorder):
        index = {ele: i for i, ele in enumerate(inorder)}
    
        def helper(post_left_idx, post_right_idx, in_left_idx, in_right_idx):
            # 终止条件
            if post_left_idx > post_right_idx:
                return None
      
            # 后序最后一个是根！（唯一区别）
            post_root_idx = post_right_idx
            in_root_idx = index[postorder[post_root_idx]]
            root = TreeNode(postorder[post_root_idx])
      
            size = in_root_idx - in_left_idx  # 左子树大小
      
            # 递归构造左子树
            root.left = helper(post_left_idx, post_left_idx + size - 1,
                                                in_left_idx, in_root_idx - 1)
      
            # 递归构造右子树
            root.right = helper(post_left_idx + size, post_right_idx - 1,
                                                    in_root_idx + 1, in_right_idx)
      
            return root
      
            return helper(0, len(postorder)-1, 0, len(inorder)-1)
