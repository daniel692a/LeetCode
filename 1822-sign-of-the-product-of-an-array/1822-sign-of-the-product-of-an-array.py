class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1 # O(1)
        for item in nums: # O(n)
            if item==0:
                return  0
            elif item<0:
                product*=-1
            else:
                product*=1
        return -1 if product<0 else 1