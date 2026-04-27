# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def first(self,l,r):
        if l==r:
            return l
        s=l+(r-l)//2
        if isBadVersion(s):
            return self.first(l,s)
        else:
            return self.first(s+1,r)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.first(1,n)