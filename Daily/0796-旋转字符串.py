# 模拟旋转
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) == len(goal) and s == goal:
            return True
        n = len(s)
        for i in range(n):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False

# 搜索子字符串
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
