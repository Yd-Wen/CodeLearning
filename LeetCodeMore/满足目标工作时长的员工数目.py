# 迭代
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        for h in hours:
            if h >= target:
                res += 1
        return res

# 二分查找        
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        hours.sort()
        if hours[-1] < target:
            return 0
        if hours[0] >= target:
            return len(hours)
        l = 0
        r = len(hours) - 1
        while l < r:
            mid = l + (r - l) // 2
            if hours[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return len(hours) - r
        