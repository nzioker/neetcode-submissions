class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(r,c):
            if r < 0 or c < 0 or r == m or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1

            if (r,c) in memo:
                return memo[(r,c)]

            paths_right = dfs(r+1,c)
            paths_down = dfs(r,c+1)

            memo[(r,c)] = paths_right + paths_down
            return memo[(r,c)]
        return dfs(0,0)

        
        