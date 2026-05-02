import collections


class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(n + 1):
            hashmap = collections.defaultdict(int)
            while i % 10 != i:
                if i % 10 in [3, 4, 7]:
                    break
                hashmap[i % 10] += 1
                i /= 10
            if i % 10 in [3, 4, 7]:
                continue
            if i % 10 == i:
                hashmap[i] += 1
            if hashmap[2] > 0 or hashmap[5] > 0 or hashmap[6] > 0 or hashmap[9] > 0:
                res += 1
        return res
    

class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]

        ans = 0
        for i in range(1, n + 1):
            num = [int(digit) for digit in str(i)]
            valid, diff = True, False
            for digit in num:
                if check[digit] == -1:
                    valid = False
                elif check[digit] == 1:
                    diff = True
            if valid and diff:
                ans += 1
        
        return ans
