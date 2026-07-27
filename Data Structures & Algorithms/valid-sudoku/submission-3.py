class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        for i in range(9):
            row.clear()
            for j in range(9):
                if  board[i][j] ==".":
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
        col = set()
        for i in range(9):
            col.clear()
            for j in range(9):
                if  board[j][i] ==".":
                    continue
                if board[j][i] in col:
                    return False
                col.add(board[j][i])
        box = set()
        for i in range(0,9,3):
            for j in range(0,9,3):
                box.clear()
                for r in range(i,i+3,1):
                    for c in range(j,j+3,1):
                        if  board[r][c] ==".":
                            continue
                        if board[r][c] in box:
                            return False
                        box.add(board[r][c])
        return True
                        
        

        
        