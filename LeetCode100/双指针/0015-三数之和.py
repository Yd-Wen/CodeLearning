import collections


class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            k = len(nums) - 1
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
        return res


import collections

class Solution2(object):
    def threeSum(self, nums):
        hashmap = collections.Counter(nums)
        nums = sorted(set(nums))
        result = []
        if hashmap[0] >2: result.append([0,0,0])
        for left in nums:
            if left>=0: break
            for right in reversed(nums):
                if right <=0: break
                mid = -left-right
                if mid>right: break
                if mid<left: continue
                if mid in hashmap:
                    if (mid==left and hashmap[left]>1) or (mid==right and hashmap[right]>1) or (mid!=left and mid!=right):result.append([left,mid,right])
        return result
      

if __name__ == "__main__":
    nums = [-100,-70,-60,110,120,130,160]
    print(Solution2().threeSum(nums))
