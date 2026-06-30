class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])
        topRow = False

        # check the row and col that need to be zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        topRow = True
        
        # change the row/ col to zero except the top row and the left col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] =0
        
        # check the top left for the left cols
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        # check the extra mem for the top row
        if topRow:
            for c in range(cols):
                matrix[0][c] = 0
