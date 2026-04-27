# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(1) == 0:
            return 1
        if guess(n) == 0:
            return n
        l = 1
        r = n
        while l <= r:
            mid = l + (r - l) / 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                r = mid
            else: 
                l = mid + 1
        return l
        