class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        for r in board:
            if self.hasDuplicate(r):
                # print("row dup")
                return False
        
        #columns
        for i in range(0,9):
            c = []
            for r in board:
                c.append(r[i])
            if self.hasDuplicate(c):
                # print("column dup")
                return False
        
        #cell
        for i in range(0, 9, 3):
            for j in range (0, 9, 3):
                cell = self.getCellList(i, j, board)
                # print(i, j)
                # print(cell)
                if self.hasDuplicate(cell):
                    return False
        
        return True

    def getCellList(self, x, y, board):
        result = []
        for i in  range (x, x+3):
            for j in range (y, y+3):
                result.append(board[i][j])
        return result

    

    def hasDuplicate(self, l: List[str]) -> bool:
        d = {}
        for s in l:
            if d.get(s) is not None and s != ".":
                # print(l, s)
                return True
            d[s] = 1
        return False
        