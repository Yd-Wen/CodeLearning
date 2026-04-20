"""
核心贪心思路
最大距离一定来自两端：
- 最远的有效对，要么是最左房子和右侧某个异色房子
- 要么是最右房子和左侧某个异色房子
- 既不在最左，也不在最右，那我们一定能把它往外扩得更远，而且颜色依然不同，矛盾
"""
class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        left = 0
        right = n - 1
        res = 1
        for i in range(n-1, -1, -1):
            if colors[i] != colors[left]:
                res = max(res, i - left)
                break
        for i in range(n):
            if colors[i] != colors[right]:
                res = max(res, right - i)
                break
        return res