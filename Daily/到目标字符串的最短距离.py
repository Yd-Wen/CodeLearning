class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        if words[startIndex] == target:
            return 0
        n = len(words)
        min_dist = n
        for i in range(n):
            if words[i] == target:
                min_dist = min(min_dist, min(abs(startIndex - i), n - abs(startIndex - i)))
        return -1 if min_dist == n else min_dist

if __name__ == "__main__":
    solution = Solution()
    print(solution.closestTarget(["hello", "i", "am", "leetcode", "hello"], "hello", 1))
    print(solution.closestTarget(["a", "b", "c", "d"], "e", 0))
