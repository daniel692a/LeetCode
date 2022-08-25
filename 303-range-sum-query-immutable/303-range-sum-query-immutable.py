class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = [] # S = O(n)
        sumPrefix = 0
        for i in range(len(self.nums)):
            sumPrefix += self.nums[i]
            self.prefixSum.append(sumPrefix)

    def sumRange(self, left: int, right: int) -> int:
        # O(q)
        if left > 0:
            return self.prefixSum[right]-self.prefixSum[left-1]
        else:
            return self.prefixSum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)