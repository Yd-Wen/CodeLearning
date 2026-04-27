"""
Kadane 算法的本质是动态规划：对于每个位置，我们只需要关心「以当前元素结尾的子数组的最大和」。
数组: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
      ↓
遍历过程:

i=0, num=-2: pre = max(0+(-2), -2) = -2,  res = max(-2, -2) = -2
i=1, num=1:  pre = max(-2+1, 1)   = 1,   res = max(-2, 1)  = 1   ← 重新开始更优
i=2, num=-3: pre = max(1+(-3), -3) = -2,  res = max(1, -2)  = 1
i=3, num=4:  pre = max(-2+4, 4)   = 4,   res = max(1, 4)   = 4   ← 重新开始更优
i=4, num=-1: pre = max(4+(-1), -1) = 3,   res = max(4, 3)   = 4   ← 延续更优
i=5, num=2:  pre = max(3+2, 2)    = 5,   res = max(4, 5)   = 5   ← 延续更优
i=6, num=1:  pre = max(5+1, 1)    = 6,   res = max(5, 6)   = 6   ← 延续更优 [最大]
i=7, num=-5: pre = max(6+(-5), -5) = 1,   res = max(6, 1)   = 6
i=8, num=4:  pre = max(1+4, 4)    = 5,   res = max(6, 5)   = 6

最终答案: 6 (子数组 [4,-1,2,1])

一句话总结
"能续就续，不能续就断，全程记录最大值"
"""
class Solution:
    def maxSubArray(self, nums):
        pre = 0           # 以当前元素结尾的子数组的最大和
        res = nums[0]     # 全局最大子数组和（初始化为第一个元素）
        
        for num in nums:
            # 关键决策：是"延续前面的子数组"还是"从当前元素重新开始"
            pre = max(pre + num, num)
            
            # 更新全局最优解
            res = max(res, pre)
        
        return res
        