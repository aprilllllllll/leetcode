class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        for x in nums:
            if x == 0:
                nums.remove(x)
                nums.append(x)


        return nums

solution = Solution()
nums =  [0,1,0,3,12]
print(solution.moveZeroes(nums))