class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)
        res = 0
        uf = UnionFind(n)
        hashmap = defaultdict(lambda: defaultdict(int))
        for ai, bi in allowedSwaps:
            uf.union(ai, bi)
        for i in range(n):
            hashmap[uf.find(i)][source[i]] += 1
        for i in range(n):
            if hashmap[uf.find(i)][target[i]] > 0:
                hashmap[uf.find(i)][target[i]] -= 1
            else:
                res += 1
        return res
        