class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[0,-1], [-1,0]]
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0
        def inBounds(row, col):
            return (row < 0 or col < 0) or (row >= ROWS or col >= COLS) or grid[row][col] != 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    perimeter += 4
                    for dr, dc in directions:
                        row, col = dr + r, dc + c
                        if inBounds(row,col):
                            continue
                        perimeter -= 2
        return perimeter
        