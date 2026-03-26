class Solution1(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur_len = 1
    max_len = 0
    nums_set = set(nums)  # 集合去重
    for num in nums_set:
      if num-1 not in nums_set:
        cur_len = 1
        while num + 1 in nums_set:
          cur_len += 1
          num += 1
        max_len = max(max_len, cur_len)
        
    return max_len
  

class Solution2(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur_len = 1
    max_len = 0
    # 去重
    nums_set = set(nums)
    # 判断数组长度
    if len(nums_set) < 2:
      return len(nums_set)

    # 排序
    nums_sort = sorted(nums_set)
    # 集合长度校验
    if nums_sort[-1] - nums_sort[0] == len(nums_sort) - 1:
      return len(nums_sort)

    # 遍历
    for i in range(len(nums_sort)-1):
      if nums_sort[i] +1 == nums_sort[i+1]:
        cur_len += 1
      else:
        max_len = max(max_len, cur_len)
        cur_len = 1
    return max(max_len, cur_len)


if __name__ == '__main__':
  s1 = Solution1()
  s2 = Solution2()
  print(s1.longestConsecutive([100,4,200,1,3,2]))
  print(s2.longestConsecutive([100,4,200,1,3,2]))
