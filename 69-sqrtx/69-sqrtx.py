class Solution:
    def mySqrt(self, x: int) -> int:
        temp, sqrt = 0, x/2
        while sqrt != temp:
            temp = sqrt
            sqrt = (x/temp + temp)/2
        
        return int(sqrt)