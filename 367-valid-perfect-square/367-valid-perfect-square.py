class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        temp, sqrt = 0, num/2
        while sqrt != temp:
            temp = sqrt
            sqrt = (num/temp + temp)/2
            
        return True if sqrt%1==0 else False
        