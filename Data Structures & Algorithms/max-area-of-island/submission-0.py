class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        def area(grid, i , j):
            count = 0
            if min(i,j) <0 or i >= r or j >= c or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            count += 1
            dirs = [(1,0),(0,1),(-1,0), (0,-1)]
            for dr, dl in dirs:
                count += area(grid, i+dr, j+dl)
            return count
        result = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    result = max(result, area(grid,i,j))
        return result
            
        