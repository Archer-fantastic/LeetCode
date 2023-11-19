class Solution(object):
    def isValidSudoku(self,board):
        for i in range(9):                        #对每一行进行判断
            storage = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in storage:
                    return False
                else:
                    storage.append(board[i][j])
        for i in range(9):                         #对每一列进行判断
            storage = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in storage:
                    return False
                else:
                    storage.append(board[j][i])
        for i in range(0, 9, 3):                   #对九宫格是否重复进行判断
            for j in range(0, 9, 3):
                storage = []
                for x in range(0, 3):
                    for y in range(0, 3):
                        if board[i + x][j + y] == '.':
                            continue
                        if board[i + x][j + y] in storage:
                            return False
                        else:
                            storage.append(board[i + x][j + y])
        return True