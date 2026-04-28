# 找中位数法
class Solution:
    def minOperations(self, grid, x):
        m, n = len(grid), len(grid[0])
        nums = list()
        for i in range(m):
            for j in range(n):
                if (grid[i][j] - grid[0][0]) % x != 0:
                    return -1
                nums.append(grid[i][j])

        nums.sort()
        choose = nums[len(nums) // 2]
        ans = 0
        for num in nums:
            ans += abs(num - choose) // x
        return ans
