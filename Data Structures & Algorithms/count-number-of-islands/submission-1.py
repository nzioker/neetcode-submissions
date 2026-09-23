class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited_islands = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r,c) in visited_islands:
                return False
            visited_islands.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited_islands:    
                    islands += 1
                    dfs(r,c)

        return islands
        
        

        