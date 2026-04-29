class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return n - 1
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) / 2
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if target < nums[0] < nums[mid]:
                    l = mid + 1
                else: r = mid - 1
            else:
                if target > nums[-1] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
