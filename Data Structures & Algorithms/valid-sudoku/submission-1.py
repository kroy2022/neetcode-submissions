class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkColumn(xIndex):
            i = 0
            dup = set()
            while i < len(board):
                if board[i][xIndex] != ".":
                    if board[i][xIndex] in dup:
                        return False
                    
                dup.add(board[i][xIndex])
                i += 1
            
            return True

        def checkRow(yIndex):
            dup = set()
            for i in range(len(board[yIndex])):
                if board[yIndex][i] != ".":
                    if board[yIndex][i] in dup:
                        return False
                
                dup.add(board[yIndex][i])

            return True
        
        def checkGrid(x, y):
            dup = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] != ".":
                        if board[i][j] in dup:
                            return False
                    
                    dup.add(board[i][j])

            return True
        
        # Check every row and column
        for i in range(9):
            if not checkRow(i) or not checkColumn(i):
                return False
            
        # Check every grid (0, 0) (0, 3) (0, 6) (3, 0) (3, 3) (3, 6) (6, 0) (6, 3) (6, 6)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkGrid(i, j):
                    return False

        return True
