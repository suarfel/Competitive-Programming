class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
            
        def row_checker():
            for row in board:
                temp = []
                for val in row:
                    if val != '.':
                        temp.append(val)
                if len(temp) != len(set(temp)):
                    return False
            return True
        
        def column_checker():
            for i in range(len(board[0])):
                temp = []
                for j in range(len(board)):
                    if board[j][i] != '.':
                        temp.append(board[j][i])
                    if len(temp) != len(set(temp)):
                        return False
            return True
        
        if not (row_checker() and column_checker()):
            return False
        
        def three_by_three_checker(row,col):
            temp = []
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if board[i][j] != '.':
                        temp.append(board[i][j])
            return len(temp) == len(set(temp))
        
        i,j = 0,0
        while i < 9:
            while j < 9:
                truth_val = three_by_three_checker(i,j)
                if not truth_val:
                    return False
                j += 3
            i += 3
            j = 0
            
        return True
                
                
            
        
        