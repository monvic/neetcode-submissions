class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rd = defaultdict(set)
        cd = defaultdict(set)
        bd = defaultdict(set)

        for i in range(9):
            for j in range(9):
                el = board[i][j]
                if el == ".":
                    continue
                if (el in rd[i]) or (el in cd[j]) or (el in bd[(i//3, j//3)]):
                    return False
                rd[i].add(el)
                cd[j].add(el)
                bd[(i//3, j//3)].add(el)
        
        return True