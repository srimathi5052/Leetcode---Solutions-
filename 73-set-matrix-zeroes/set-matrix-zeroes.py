class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        first_row = False
        first_col = False

        # Check if first row has a zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                break

        # Check if first column has a zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if first_col:
            for i in range(m):
                matrix[i][0] = 0