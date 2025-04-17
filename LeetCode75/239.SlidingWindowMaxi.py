class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_nums=[]
        for i in range(0,len(nums)-k+1):
            max_nums.append(max(nums[i:i+k]))

        return max_nums

solution = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k=3
print(solution.maxSlidingWindow(nums,k))
