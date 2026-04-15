from typing import List
import collections

"""
【题目】
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
]

【代码详解】

# 创建一个默认值为列表的字典，键不存在时值会创建一个空列表
mp = collections.defaultdict(list) 

# ord(ch)：字母 → ASCII 码，a → 0，b → 1，... z → 25
counts[ord(ch) - ord("a")] += 1    

# 创建键值对，计数数组当作哈希表的 key（转为不可变的元组后，才能用作 key），值为列表
mp[tuple(counts)].append(st)       
"""

# 1. 排序
class Solution1(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = collections.defaultdict(list)
        for s in strs:
            # 排序结果作为key ''.join将列表转为字符串（列表不能用作key）
            mp[''.join(sorted(s))].append(s)
        return list(mp.values())

# 2. 计数
class Solution2(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
                counts = [0] * 26
                for ch in st:
                        counts[ord(ch) - ord("a")] += 1
                # 次数列表作为key，需要将 list 转换成 tuple 才能进行哈希
                mp[tuple(counts)].append(st)
    
        return list(mp.values())


# 3. 质数乘积
class Solution3(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    
        result = {}  # 字典：键是质数乘积，值是单词列表
    
        for word in strs:
                # 计算每个单词的质数乘积（作为唯一标识）
                product = 1
                for char in word:
                        index = ord(char) - ord('a')  # 获取字母位置（0-25）
                        product *= primes[index]      # 乘以对应的质数
        
                # 将单词添加到对应的组中
                if product in result:
                        result[product].append(word)
                else:
                        result[product] = [word]
    
        # 返回所有分组
        return list(result.values())


if __name__ == '__main__':
    s = Solution3()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
