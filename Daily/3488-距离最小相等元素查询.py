# 哈希表 + 二分查找
class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        nums_pos = defaultdict(list)

        for i in range(n):
            nums_pos[nums[i]].append(i)

        for pos in nums_pos.values():
            x = pos[0]
            pos.insert(0, pos[-1] - n)
            pos.append(x + n)

        for i in range(len(queries)):
            x = nums[queries[i]]
            pos_list = nums_pos[x]
            if len(pos_list) == 3:
                queries[i] = -1
                continue
            pos = bisect.bisect_left(pos_list, queries[i])
            queries[i] = min(pos_list[pos + 1] - pos_list[pos], pos_list[pos] - pos_list[pos - 1])

        return queries

# 预处理左右最近元素位置 + 哈希表
class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        left = [0] * n
        right = [0] * n
        pos = {}
        
        # 循环范围是 -n 到 n-1，插入虚拟左位置，模拟环形数组的效果，从左到右遍历，找到与最近相同左元素索引
        for i in range(-n, n):
            if i >= 0:
                left[i] = pos.get(nums[i]) # 真实索引位置，找到最近相同元素位置
            pos[nums[(i + n) % n]] = i  # 记录位置

        pos.clear()
        # 循环范围是 2n-1 到 0，插入虚拟右位置，模拟环形数组的效果，从右到左遍历，找到与最近相同右元素索引
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                right[i] = pos.get(nums[i]) # 真实索引位置，找到最近相同元素位置
            pos[nums[i % n]] = i  # 记录位置

        for i in range(len(queries)):
            x = queries[i]
            # 当前查询位置与左边最近的值相等的元素位置的距离是否等于数组长度，如果相等的话说明这个元素只在数组中出现了一次
            if x - left[x] == n:
                queries[i] = -1
            else:
                queries[i] = min(x - left[x], right[x] - x)

        return queries
