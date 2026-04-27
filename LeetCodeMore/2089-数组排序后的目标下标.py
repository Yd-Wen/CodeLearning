# 迭代
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0 or (n == 1 and nums[0] != target):
            return []
        nums.sort()
        if nums[-1] < target or nums[0] > target:
            return []
        res = []
        for i in range(n):
            if nums[i] == target:
                res.append(i)
        return res
    

# 二分查找
class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0 or (n == 1 and nums[0] != target):
            return []
        nums.sort()
        if nums[-1] < target or nums[0] > target:
            return []
        l, r = 0, n - 1
        res = []
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] > target: return []
        res = [l, r] if l != r else [l]
        while r + 1 < n and nums[r + 1] == target:
            r += 1
            res.append(r)
        return res
        