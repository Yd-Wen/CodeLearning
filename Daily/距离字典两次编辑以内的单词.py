class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        q_len = len(queries)
        d_len = len(dictionary)
        n = len(queries[0])
        if n < 3: return queries
        res = []
        for q in queries:
            for d in dictionary:
                diff = 0
                for i in range(n):
                    if q[i] != d[i]:
                        diff += 1
                    if diff > 2:
                        break
                if diff <= 2: 
                    res.append(q)
                    break
        return res
       