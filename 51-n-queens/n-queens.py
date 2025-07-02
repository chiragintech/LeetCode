from typing import List

def isSafe(row, col, board, n):
    # Check vertically up
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    maxLeft = min(row, col)
    for i in range(maxLeft + 1):
        if board[row-i][col-i] == 'Q':
            return False

    # Check upper-right diagonal
    maxRight = min(row, len(board) - col - 1)
    for i in range(maxRight + 1):
        if board[row-i][col+i] == 'Q':
            return False

    return True

def solve(row, board, ans, n):
    if row == n:
        # Convert board to list of strings
        ans.append([''.join(r) for r in board])
        return

    for col in range(n):
        if isSafe(row, col, board, n):
            board[row][col] = 'Q'
            solve(row + 1, board, ans, n)
            board[row][col] = '.'

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(0, board, ans, n)
        return ans
