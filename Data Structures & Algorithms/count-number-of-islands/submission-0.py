from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            while q:
                curr_r, curr_c = q.popleft()

                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc

                    if (nr in range(rows) and nc in range(cols) and 
                        grid[nr][nc] == "1" and (nr, nc) not in visited):
                        
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count