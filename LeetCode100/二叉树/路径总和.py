class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 前缀和字典：key=前缀和，value=出现次数
        prefix = collections.defaultdict(int)
        prefix[0] = 1  # 初始化：前缀和 0 出现 1 次（很重要）

        # DFS 遍历，curr = 从根到当前节点的累计和
        def dfs(root, curr):
            if not root: return 0  # 空节点返回 0
            ret = 0

            curr += root.val  # 当前累计和 += 节点值

            # ✅ 核心：看看之前有多少个前缀和 = curr - target
            # 有多少个，就有多少条路径满足和为 target
            ret += prefix[curr - targetSum]

            # ✅ 把当前前缀和加入字典
            prefix[curr] += 1

            # ✅ 递归左右子树
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)

            # ✅ 回溯！非常重要！
            # 离开这个节点，要撤销当前前缀和（保证不影响其他左/右分支）
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)