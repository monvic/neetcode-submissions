class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])
        dirs = [(1,0), (0,1),(-1,0), (0,-1)]
        def calc_distance(grid, i, j):
            q = deque()
            dist = 1
            visited = set()
            q.append((i,j))
            while q:
                for l in range(len(q)):
                    x,y = q.popleft()
                    visited.add((x,y))
                    for dr, dc in dirs:
                        if min(x+dr,y+dc)>=0 and x+dr<r and y+dc<c  and grid[x+dr][y+dc] != 0 and grid[x+dr][y+dc] != -1  and (x + dr, y + dc) not in visited:           
                            grid[x+dr][y+dc]=min(grid[x+dr][y+dc], dist )
                            q.append((x+dr, y+dc))
                dist += 1
 

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    calc_distance(grid, i,j)
        
        # return grid

        