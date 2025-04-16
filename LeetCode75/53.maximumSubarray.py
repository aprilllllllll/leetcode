class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]


        maxSum = nums[0]


        for n in nums:
            c = c+n
            maxSum = max(maxSum,c)
            if c<0:
                c=0




        return maxSum




solution = Solution()

nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]

print(solution.maxSubArray(nums))