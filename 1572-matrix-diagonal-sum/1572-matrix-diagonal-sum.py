class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonals_sum = 0
        j = len(mat)-1
        for i in range(len(mat)):
            if i==j:
                diagonals_sum += mat[i][i]    
            else:
                diagonals_sum += (mat[i][i] + mat[i][j])
            j-=1
        return diagonals_sum
        