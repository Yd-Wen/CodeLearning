class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)
        max_dist = i = j = 0
        while i < n:
            j = i + max_dist + 1
            while j < m:
                if nums1[i] <= nums2[j]:
                    max_dist = max(max_dist, j - i)
                    j += 1
                else:
                    break
            i += 1

        return max_dist


class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)
        i = j = 0
        while i < n and j < m:
            if nums1[i] > nums2[j]:
                i += 1
            j += 1
        return j - i -1 if j - i - 1 >= 0 else 0  # 退出循环，指针越界
