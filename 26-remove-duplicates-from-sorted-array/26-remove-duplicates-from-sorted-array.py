class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_duplicate = len(nums)-1
        current = nums[0]
        k = 1
        has_duplicates = False
        for i in range(1, len(nums)):
            if nums[i]==current:
                last_duplicate = min(last_duplicate, i)
                nums[i] = None
                has_duplicates = True
            else:
                k+=1
                current = nums[i]
                if has_duplicates:
                    nums[last_duplicate], nums[i] = nums[i], nums[last_duplicate]
                    last_duplicate+=1
        return k
            