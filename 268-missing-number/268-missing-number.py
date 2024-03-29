class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        complete_sum = (len(nums)*(len(nums)+1))//2 # O(1)
        cumulative_sum = 0
        for item in nums: #O(n)
            cumulative_sum += item
        return complete_sum-cumulative_sum
        