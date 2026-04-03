class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        pacific_ocean = [[0 for col in range(c)] for row in range(r)]
        atlantic_ocean = [[0 for col in range(c)] for row in range(r)]

        def fill_q_grid(p_grid, p, a_grid, a):
            for i in range(c):
                p_grid[0][i] = 1
                p.append((0,i))
                a_grid[r-1][i] = 1
                a.append((r-1,i))
            for i in range(r-1):
                p_grid[i+1][0] = 1
                p.append((i+1,0))
                a_grid[i][c-1] = 1
                a.append((i,c-1))

        q_pacific = deque()
        q_atlantic = deque()
        

        fill_q_grid(pacific_ocean, q_pacific, atlantic_ocean, q_atlantic)


        def in_grid(x,y):
            if min(x,y) >= 0 and x <r and y<c:
                return True
            else:
                return False

        def fill_water(q, h_grid, q_grid):
            visited = set()
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    visited.add((x,y))
                    for dr, dc in dirs:
                        dx = x+dr
                        dy = y+dc
                        # print(dx,dy)
                        if in_grid(dx,dy) and h_grid[dx][dy]>=h_grid[x][y] and (dx, dy) not in visited and q_grid[dx][dy] == 0:
                            q_grid[dx][dy] = 1
                            q.append((dx,dy))
        
        fill_water(q_pacific, heights, pacific_ocean)
        # print(pacific_ocean)
        fill_water(q_atlantic, heights, atlantic_ocean)
        # print(atlantic_ocean)
        
        result = []
        for i in range(r):
            for j in range(c):
                if pacific_ocean[i][j] == 1 and  atlantic_ocean[i][j] == 1:
                    result.append([i,j])
        return result




                