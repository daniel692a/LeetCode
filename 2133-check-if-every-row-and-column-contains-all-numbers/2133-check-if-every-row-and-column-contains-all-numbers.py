class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row_set = set() # O(n)
        column_set = set() # O(n)
        
        ## check columns
        for i in range(len(matrix)): #O(n^3)
            row_set = set(matrix[i])
            if len(row_set) != len(matrix):
                return False
            row_set.clear()
            for x in range(len(matrix)):
                for j in range(len(matrix)):
                    column_set.add(matrix[j][x])
                if len(column_set)!=len(matrix):
                    return False
                column_set.clear()

        return True
        