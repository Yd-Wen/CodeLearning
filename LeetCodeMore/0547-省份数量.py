class UnionFind(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1: 
                    uf.union(i, j)
        return sum(uf.find(i) == i for i in range(n))


# 官方题解:无数据结构定义,无按秩合并
class Solution:
    def findCircleNum(self, isConnected):
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)
        
        cities = len(isConnected)
        parent = list(range(cities))
        
        for i in range(cities):
            for j in range(i + 1, cities):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        provinces = sum(parent[i] == i for i in range(cities))
        return provinces
