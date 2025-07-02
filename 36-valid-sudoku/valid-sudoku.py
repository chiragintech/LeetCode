from typing import List

def is_valid(board, row, col):
    val = board[row][col]
    if val == '.':
        return True 
    for i in range(9):
        if i != col and board[row][i] == val:
            return False
        if i != row and board[i][col] == val:
            return False
        r = 3 * (row // 3) + i // 3
        c = 3 * (col // 3) + i % 3
        if (r != row or c != col) and board[r][c] == val:
            return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if not is_valid(board, i, j):
                    return False
        return True
