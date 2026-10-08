from itertools import combinations
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(p):
            if p == 1: return 1
            if p == 2: return 2

            if p in memo:
                return memo[p]

            memo[p] = dfs(p - 1) + dfs(p - 2)
            return memo[p]
        return dfs(n)
        