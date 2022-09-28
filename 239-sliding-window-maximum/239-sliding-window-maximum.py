class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        l = r = 0
        queueMax = collections.deque() # O(n)
        while r<len(nums): # O(n)
            while queueMax and nums[queueMax[-1]] < nums[r]:
                queueMax.pop()
            queueMax.append(r)
            if l>queueMax[0]:
                queueMax.popleft()
            
            if (r+1) >= k:
                answer.append(nums[queueMax[0]])
                l+=1
            r+=1
            
        return answer