from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        queue.append((0,0))
        visited.add((0,0))

        length = 1

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                if r == (ROWS - 1) and c == (COLS - 1):
                    return length

                directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]

                for dr,dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 1 or (nr,nc) in visited:
                        continue 
                    queue.append((nr,nc))
                    visited.add((nr,nc))
            length += 1
        return -1
        