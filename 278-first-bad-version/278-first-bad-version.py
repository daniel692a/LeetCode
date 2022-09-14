# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        pos = -1 #O(1)
        while start<=end: #O(logn)
            mid = start + ((end-start)//2)
            if isBadVersion(mid):
                pos = mid
                end = mid-1
            else:
                start = mid+1
        return pos
            
        