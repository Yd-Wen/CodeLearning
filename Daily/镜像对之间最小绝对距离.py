# nums = [12,2,21,4,66,78,21] 不通过，字典覆盖了旧值，只保留了最后一次出现的下标
class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_reverse(num):
            # 转字符串反转
            reversed_str = str(num)[::-1]
            # 转回数字
            return int(reversed_str)
        
        n = len(nums)
        if n == 1: return -1
        res = n
        hashmap = {}

        for i in range(n):
            if hashmap.get(get_reverse(nums[i])):
                res = min(res, i - hashmap.get(get_reverse(nums[i])))
            hashmap[nums[i]] = i
        for i, num in enumerate(nums):
            if hashmap.get(get_reverse(num)) != None:
                print(hashmap.get(get_reverse(num)))  
            if hashmap.get(get_reverse(num)) != None and hashmap.get(get_reverse(num)) > i:
                res = min(res, hashmap.get(get_reverse(num)) - i)
        return res if res !=n else -1

class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_reverse(num):
            # 转字符串反转
            reversed_str = str(num)[::-1]
            # 转回数字
            return int(reversed_str)

            return int(str(num)[::-1])
        
        n = len(nums)
        if n == 1: return -1
        res = n
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap:
                res = min(res, i-hashmap[num])
            hashmap[get_reverse(num)] = i
        return res if res !=n else -1
