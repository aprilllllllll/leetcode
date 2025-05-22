from collections import deque
from unittest import result


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        res = []
        l=0
        r =0
        while r<len(nums):
            
            while dq and nums[dq[-1]]<nums[r]:
                dq.pop()
            dq.append(r)

            if l>dq[0]:
                dq.popleft()

            if r+1>=k:
                res.append(nums[dq[0]])
                l+=1
            r+=1
        return res




solution = Solution()
nums = [7,2,4]
k=2
print(solution.maxSlidingWindow(nums,k))
