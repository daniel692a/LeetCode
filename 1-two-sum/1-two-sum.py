class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {} # space: O(n)
        for i, n in enumerate(nums): # time: O(n)
            difference = target - n
            if difference in previousMap:
                return [previousMap[difference], i]
            previousMap[n] = i
        return -1
        