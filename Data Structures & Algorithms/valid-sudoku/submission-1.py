class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s1 = set() #check for row
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s1:
                    return False
                else:
                    s1.add(board[i][j])
            
        for i in range(9):
            s1 = set() #check for column
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in s1:
                    return False
                else:
                    s1.add(board[j][i])
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                s1 = set()
                for r in range(i,i+3,1):
                    for c in range(j,j+3,1):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in s1:
                            return False
                        else:
                            s1.add(board[r][c])
            return True