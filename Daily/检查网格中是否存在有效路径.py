# 并查集
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        if self.find(x) == self.find(y):
            return
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        def getId(x, y):
            return x * n + y
        
        def detectL(x, y):
            if y - 1 >= 0 and grid[x][y - 1] in [1, 4, 6]:
                uf.union(getId(x, y), getId(x, y - 1))
        
        def detectR(x, y):
            if y + 1 < n and grid[x][y + 1] in [1, 3, 5]:
                uf.union(getId(x, y), getId(x, y + 1))
        
        def detectU(x, y):
            if x - 1 >= 0 and grid[x - 1][y] in [2, 3, 4]:
                uf.union(getId(x, y), getId(x - 1, y))
        
        def detectD(x, y):
            if x + 1 < m and grid[x + 1][y] in [2, 5, 6]:
                uf.union(getId(x, y), getId(x + 1, y))

        def handler(x, y):
            if grid[x][y] == 1:
                detectL(x, y)
                detectR(x, y)
            elif grid[x][y] == 2:
                detectU(x, y)
                detectD(x, y)
            elif grid[x][y] == 3:
                detectL(x, y)
                detectD(x, y)
            elif grid[x][y] == 4:
                detectR(x, y)
                detectD(x, y)
            elif grid[x][y] == 5:
                detectL(x, y)
                detectU(x, y)
            else:
                detectR(x, y)
                detectU(x, y)
        
        for i in range(m):
            for j in range(n):
                handler(i, j)
        
        return uf.find(getId(0, 0)) == uf.find(getId(m - 1, n - 1))
    
# DFS
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        direction = {1:{(0,1),(0,-1)}, 2:{(1,0),(-1,0)},3:{(0,-1),(1,0)},4:{(0,1),(1,0)},5:{(0,-1),(-1,0)},6:{(0,1),(-1,0)}}
    # 每个数字对应的方向先列出
        n = len(grid)
        n1 = len(grid[0])
        flag = [[0] * n1 for i in range(n)]
        def dfs(i,j):
            flag[i][j] = 1
            if i == n - 1 and j == n1 - 1:return True
            for x,y in direction[grid[i][j]]:
                if 0 <= i + x < n and 0 <= j + y < n1 and flag[i + x][y + j] == 0 and (-x,-y) in direction[grid[i + x][j + y]]:
                # 0 <= i + x < n and 0 <= j + y < n1 是为了在范围内限制 
                # 判断flag[i + x][y + j] 是为了不重复走循环路
                # 精髓：(-x,-y) in direction[grid[i + x][j + y]] 表示可以走的连通路
                    if dfs(i + x,j + y): return True
            return False
        return dfs(0,0)
