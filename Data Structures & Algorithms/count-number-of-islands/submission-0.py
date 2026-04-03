class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        def fill(grid, i, j):
            if min(i,j) < 0 or i>= ROWS or j>=COLS or grid[i][j] != "1":
                return
            grid[i][j] = "2"
            direc = [(1,0), (0,1), (-1, 0), (0,-1)]
            for dr, dl in direc:
                fill(grid, i+dr, j+dl)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    result += 1 
                    fill(grid, i , j)
        
        return result
                