class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        if n == 2:
            if k % 2 == 0:
                return
            else:
                nums[:] = nums[::-1]
                return
        if k % n == 0:
            return nums
        for i in range(n - k % n):
            nums.append(nums[i])
        nums[:] = nums[n - k % n:]
        