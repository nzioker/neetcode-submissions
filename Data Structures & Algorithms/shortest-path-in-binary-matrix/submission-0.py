from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        # Edge cases when start and target cell == 1
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        visited.add((0,0))
        queue.append((0,0))

        length = 1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr,nc) in visited:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1

        