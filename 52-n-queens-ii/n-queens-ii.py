def isSafe(row, col, board, n):
    # vertically up
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    # left diagonal
    maxLeft = min(row, col)
    for i in range(maxLeft + 1):
        if board[row-i][col-i] == 'Q':
            return False
    # right diagonal
    maxRight = min(row, len(board) - col - 1)
    for i in range(maxRight + 1):
        if board[row-i][col+i] == 'Q':
            return False
    return True
def solve(row, board, ans, n):
    if row == n:
        return 1
    count = 0
    for col in range(n):
        if isSafe(row, col, board, n):
            board[row][col] = 'Q'
            count += solve(row + 1, board, ans, n)
            board[row][col] = '.'
    return count

class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        return solve(0, board, ans, n)
