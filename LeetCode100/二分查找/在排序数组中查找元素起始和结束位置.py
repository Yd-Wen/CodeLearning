# 二分查找 边界模板
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0 or nums[0] > target:
            return [-1, -1]
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        # nums[l] >= target
        if nums[l] != target: return [-1, -1]
        while r + 1 < n and nums[r + 1] == target:
            r += 1
        return [l, r]


# 二分查找 匹配模板
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0 or nums[0] > target:
            return [-1, -1]
        l, r = 0, n - 1
        idx = -1
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        # 没有精准匹配到
        if idx == -1: return [-1, -1]
        # 查找左右边界
        l = r = mid
        while r + 1 < n and nums[r + 1] == target:
            r += 1
        while l - 1 >= 0 and nums[l - 1] == target:
            l -= 1 
        return [l, r]
    