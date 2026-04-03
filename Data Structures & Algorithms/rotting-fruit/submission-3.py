class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        def in_grid(x, y):
            if min(x,y) >=0 and x < r and y<c:
                return True
            else:
                return False
        
        def grid_had_fresh(grid):
            for i in range(r):
                for j in range(c):
                    if grid[i][j] == 1:
                        return True
            return False


        q = deque()
        visited = set()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))

        time = -1
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            print(q)
            d_r= []
            rotten = False
            for l in range(len(q)):
                x, y = q.popleft()
                
                if in_grid(x,y) and grid[x][y] != 0:
                    grid[x][y]=2
                    d_r.append((x,y))
                    for dr, dc in dirs:
                        if in_grid(x+dr, y+dc) and (x+dr, y+dc) not in visited and grid[x+dr][y+dc] == 1:
                            q.append((x+dr, y+dc))
                            visited.add((x+dr, y+dc))
            
            print(d_r)
            time += 1
        
        print(grid)
        if grid_had_fresh(grid):
            return -1
        elif time == -1:
            return 0
            
        return time 
            



        