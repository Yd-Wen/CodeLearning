class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        if nums[-1] == target:
            return len(nums) - 1
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else: 
                low = mid
            if high - low == 1:
                return high      