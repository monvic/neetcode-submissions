class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])
        dirs = [(1,0), (0,1),(-1,0), (0,-1)]
        def calc_distance(grid, i, j):
            q = deque()
            visited = set()
            dist = 0
            q.append((i,j))
            while q:
                for l in range(len(q)):
                    x,y = q.popleft()
                    visited.add((x,y))
                    if min(x,y)>=0 and x<r and y<c and grid[x][y]!=-1:
                        grid[x][y] = min(grid[x][y], dist)
                        for dr, dc in dirs:
                            if (x+dr,y+dc) not in visited:
                                q.append((x+dr, y+dc))
                dist += 1

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    calc_distance(grid, i,j)
        

        