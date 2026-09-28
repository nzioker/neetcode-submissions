from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        fresh_count = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        directions = [[1,0],[0,1],[-1,0],[0,-1]]   
        
        while queue:
            minutes += 1

            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr,nc))
        
        if fresh_count == 0:
            return minutes - 1
        else:
            return -1



        