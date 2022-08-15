class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        x_ptr, y_ptr = 0, len(grid)-1
        
        def isZero(n):
            return (n==0)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ((j == x_ptr) and (grid[i][x_ptr]==0)):
                    return False
                elif ((j == y_ptr) and (grid[i][y_ptr]==0)):
                    return False
                elif (((j!=x_ptr) and (j!=y_ptr)) and grid[i][j]!=0):
                    return False
               
            x_ptr+=1
            y_ptr-=1
        return True
        