"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 变位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

变位词 指字母相同，但排列不同的字符串。

示例 1：

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的变位词。
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        s_len = len(s)
        p_len = len(p)
        s_count = [0] * 26
        p_count = [0] * 26

        if s_len < p_len: return []

        for i in range(p_len):
            p_count[ord(p[i])-97] += 1  # ord('a') = 97
            s_count[ord(s[i])-97] += 1

        for i in range(s_len-p_len+1):
            if i > 0:
                s_count[ord(s[i-1])-97] -= 1
                s_count[ord(s[i+p_len-1])-97] += 1
            if s_count == p_count:
                res.append(i)

        return res


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len: return []

        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i])-97] += 1
            count[ord(p[i])-97] -= 1
        diff = [c !=0 for c in count].count(True) # 统计非0的个数
    
        for i in range(s_len - p_len + 1):
            if i:
                if count[ord(s[i-1]) - 97] == 0: # 原来相同，移除后不同
                    diff += 1
                elif count[ord(s[i-1]) - 97] == 1: # 原来不同，移除后相同
                    diff -= 1
                count[ord(s[i-1]) - 97] -= 1

                if count[ord(s[i+p_len-1]) - 97] == 0: # 原来相同，添加后不同
                    diff += 1
                elif count[ord(s[i+p_len-1]) - 97] == -1: # 原来不同，添加后相同
                    diff -= 1
                count[ord(s[i+p_len-1]) - 97] += 1
            if not diff:
                res.append(i)
            return res

        