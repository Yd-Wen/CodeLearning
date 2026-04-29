class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 旋转 1 次
        if n > 1 and nums[0] > nums[1]:
            return nums[1]
        # 旋转 n 次
        if nums[-1] > nums[0]:
            return nums[0]
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] > nums[0]:
                l = mid + 1
            else: 
                r = mid
        return nums[l]
    

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 旋转 1 次
        if n > 1 and nums[0] > nums[1]:
            return nums[1]
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] < nums[r]:
                r = mid
            else: 
                l = mid + 1
        return nums[l]
