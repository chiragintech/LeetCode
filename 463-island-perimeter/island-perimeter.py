class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # cols
        top, left, right, bottom = 0,0,0,0
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0:
                        top = 1
                    else:
                        top = grid[i-1][j] == 0
                    if j == 0 or not grid[i][j-1]:
                        left = 1
                    else:
                        left = grid[i][j-1] == 0
                    if j == n - 1 or not grid[i][j+1]:
                        right = 1
                    else:
                        right = grid[i][j+1] == 0
                    if i == m - 1 or not grid[i+1][j]:
                        bottom = 1
                    else:
                        bottom = grid[i+1][j] == 0
                    perimeter += top + bottom + left + right
        return perimeter

