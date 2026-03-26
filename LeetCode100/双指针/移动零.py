# class Solution(object):
#   def moveZeroes(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: None Do not return anything, modify nums in-place instead.
#     """
#     count = nums.count(0)
#     for i in range(nums.count(0)):
#       nums.remove(0)
#     nums.extend([0]*count)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while left < len(nums) and right < len(nums):
            if nums[right] != 0:
                if left != right: 
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1



if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))
        