class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        complete_sum = (len(nums)*(len(nums)+1))//2
        cumulative_sum = 0
        for item in nums:
            cumulative_sum += item
        return 0 if cumulative_sum==complete_sum else complete_sum-cumulative_sum
        