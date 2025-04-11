class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
        if target not in nums:
            return -1

        else:
            return nums.index(target)

solution = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(solution.search(nums,target))
