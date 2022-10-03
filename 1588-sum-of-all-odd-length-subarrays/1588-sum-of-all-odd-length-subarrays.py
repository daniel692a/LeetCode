class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        prefixSum = [0] * len(nums)
        answer = 0
        for i in range(len(nums)):
            answer += nums[i]
            prefixSum[i] = answer
        size_odd = 3
        while size_odd <= len(nums):
            left, right = 0, size_odd-1
            while right <= len(nums)-1:
                if left == 0:
                    answer+=prefixSum[right]
                else:
                    answer += (prefixSum[right]-prefixSum[left-1])
                right+=1
                left+=1
            size_odd  +=2
        return answer