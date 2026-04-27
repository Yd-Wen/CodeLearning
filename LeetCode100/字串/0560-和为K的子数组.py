class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_map = {0: 1}  #  key:前缀和  value:出现次数
        prefix_sum = 0
        count = 0
    
        for num in nums:
            prefix_sum += num  # 计算当前前缀和
      
            # 核心：如果 prefix_sum - k 存在，说明有子数组和为k
            if (prefix_sum - k) in prefix_map:
                count += prefix_map[prefix_sum - k]
      
            # 把当前前缀和加入哈希表
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    
        return count

if __name__ == '__main__':
        s = Solution()
        print(s.subarraySum([1,1,1], 2))
