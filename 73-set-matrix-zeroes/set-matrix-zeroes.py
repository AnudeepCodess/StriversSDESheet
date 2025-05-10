# Brute Force
# class Solution:
#     def setRow(self, matrix, m, n, i):
#         for j in range(n):
#             if matrix[i][j] != 0:
#                 matrix[i][j] = -1700
#         return matrix


#     def setColumn(self, matrix, m, n, j):
#         for i in range(m):
#             if matrix[i][j] != 0:
#                 matrix[i][j] = -1700
#         return matrix
    
    
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         r = len(matrix) # num of rows
#         c = len(matrix[0]) # num of columns
#         for i in range(r):
#             for j in range(c):
#                 if(matrix[i][j] == 0):
#                     # matrix[i][j] = -1
#                     self.setRow(matrix, r, c, i)
#                     self.setColumn(matrix, r, c, j)
                    
#         for i in range(r):
#             for j in range(c):
#                 if matrix[i][j] == -1700:
#                     matrix[i][j] = 0
                    
#         return matrix  

# Better Solution:
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # num of rows
        n = len(matrix[0]) # num of columns
        r = []
        c = []
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                   r.append(i)
                   c.append(j)

                  
        r= set(r)
        c= set(c)
        for j in range(n):
            for i in r:
                matrix[i][j] = 0
       
        for i in range(m):
            for j in c:
                matrix[i][j] = 0
        
        
        