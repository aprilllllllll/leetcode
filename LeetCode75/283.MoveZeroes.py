class Solution(object):
    def moveZeroes(self, nums):

        for x in nums:
            if x == 0:
                nums.remove(x)
                nums.append(x)


        return nums

solution = Solution()
nums =  [0,1,0,3,12]
print(solution.moveZeroes(nums))
