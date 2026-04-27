# 迭代
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix[0][0] == target:
            return True
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False        
        

# 两次二分查找
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix[0][0] == target:
            return True
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1
        while l <= r:
            mid = l + (r - l) / 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] == target:
                return True
            else:
                l = mid + 1
        x = l - 1
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) / 2
            if matrix[x][mid] > target:
                r = mid - 1
            elif matrix[x][mid] == target:
                return True
            else:
                l = mid + 1

        return False        
        

# 一次二分查找
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix[0][0] == target:
            return True
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) / 2
            if matrix[mid / n][mid % n] > target:
                r = mid - 1
            elif matrix[mid / n][mid % n] == target:
                return True
            else:
                l = mid + 1

        return False     
            