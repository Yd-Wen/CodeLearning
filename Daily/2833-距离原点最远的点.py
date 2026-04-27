class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        hashmap = defaultdict(int)
        for m in moves:
            hashmap[m] += 1
        return abs(hashmap['L'] - hashmap['R']) + hashmap['_']

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('R') - moves.count('L')) + moves.count('_')
