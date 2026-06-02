class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return -1
        rows, cols = len(grid), len(grid[0])

        def check_empty():
            for x in range(rows):
                for y in range(cols):
                    if grid[x][y] != 0:
                        return False
            return True

        if check_empty():
            return 0

        q = deque()

        def in_grid(x,y):
            if 0 <= x < rows and 0 <= y < cols:
                return True
            return False

        def check_fresh():
            for x in range(rows):
                for y in range(cols):
                    if grid[x][y] == 1:
                        return False
            return True



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))

        result = 0
        dir = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            result += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr, dc in dir:
                    nr = i+dr
                    nc = j+dc
                    # print(nr, nc)
                    if in_grid(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))



        if not check_fresh():
            # print(grid)
            return -1
        return result-1
        
        