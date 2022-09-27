class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_element = nums[0]
        for i in range(1, len(nums)):
            unique_element = unique_element ^ nums[i]
        return unique_element
        