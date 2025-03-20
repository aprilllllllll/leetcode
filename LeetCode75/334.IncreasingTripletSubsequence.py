
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')
        for x in nums:
            if x<= first:
                first = x
            elif x<= second:
                second = x
            else:
                return True
        return False
solution = Solution()
nums = [2,1,5,0,4,6]
print(solution.increasingTriplet(nums))
