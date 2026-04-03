class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])
        q = deque()
        zero = set()
        visit = set()
        for i in range(c):
            if board[0][i] == 'O':
                q.append((0,i))
                visit.add((0,i))
                zero.add((0,i))
            if board[r-1][i] == 'O':
                q.append((r-1,i))
                visit.add((r-1,i))
                zero.add((r-1,i))
        for i in range(r):
            if board[i][0]=='O':
                q.append((i,0))
                visit.add((i,0))
                zero.add((i,0))
            if board[i][c-1]=='O':
                q.append((i,c-1))
                visit.add((i,c-1))
                zero.add((i,c-1))
        
        # print(zero)
        # print(visit)
        def in_grid(x,y):
            if min(x,y)>= 0 and x < r and y <c:
                return True
            else:
                return False

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for dr, dc in dirs:
                    dx= x+dr
                    dy= y+dc
                    if in_grid(dx,dy) and ((dx,dy)) not in visit and board[dx][dy] == 'O':
                        zero.add((dx, dy))
                        visit.add((dx,dy))
                        q.append((dx,dy))
        
        # print(zero)
        for i in range(r):
            for j in range(c):
                if ((i,j)) not in zero:
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'
        # print(board)



                    
        