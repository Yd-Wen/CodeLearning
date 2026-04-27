class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        if nums[0] >= k:
            return 0
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] >= k:
                r = mid
            else:
                l = mid + 1
        return l