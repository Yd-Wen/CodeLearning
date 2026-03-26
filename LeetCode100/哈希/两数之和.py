from typing import List

# 1. 暴力求解 O(n^2) O(1)
class Solution1(object):
  def twoSum(self, nums: List[int], target:int)-> List[int]:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    for i in range(n):
      for j in range(i+1,n):
        if nums[i] + nums[j] == target:
          return [i,j]
    
    return []
        
# 2. hash 表 O(n) O(n)
# 时间复杂度：O(N)，其中 N 是数组中的元素数量。对于每一个元素 x，我们可以 O(1) 地寻找 target - x。
# 空间复杂度：O(N)，其中 N 是数组中的元素数量。主要为哈希表的开销。
# class Solution2(object):
#   def twoSum(self, nums: List[int], target:int)-> List[int]:
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     hashmap = {}                          # 创建空哈希表（字典）
#     for i, num in enumerate(nums):        # 遍历数组：i=下标，num=数字
#       # 核心：当前数在不在哈希表里
#       if target - num in hashmap:
#           # 如果在 → 直接返回两个下标
#           return [hashmap[target - num], i]
#       # 如果不在 → 把 当前数:当前下标 存进哈希表
#       hashmap[num] = i
#     return []
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
          # if(target-num in hashmap):
          if(hashmap.get(target-num) != None):
            return [hashmap[target-num], i]
          hashmap[num] = i
        return []

if __name__ == "__main__":
  nums = [2,7,11,15]
  target = 9
  print(Solution1().twoSum(nums, target))
  print(Solution().twoSum(nums, target))
