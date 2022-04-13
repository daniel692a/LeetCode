class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_appears = {x: 0 for x in nums}
        for num in nums:
            count_appears[num] += 1
        
        for key, value in count_appears.items():
            if value >= 2:
                return True
        return False
        