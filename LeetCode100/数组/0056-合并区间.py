class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        start_nums = []
        end_nums = []
        res = []
        for [start, end] in intervals:
            start_nums.append(start)
            end_nums.append(end)
        start_nums.sort()
        end_nums.sort()
        i = j = 0
        while i < n:
            start = start_nums[i]
            while i + 1 < n and end_nums[j] >= start_nums[i + 1]:
                i += 1 
                j = i
            end = end_nums[j]
            res.append([start, end])
            i += 1
            j += 1  
        return res
    

# 官方题解
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0]) # 按照start排序

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
