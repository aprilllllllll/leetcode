from tkinter import S
from turtle import right


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        left = [1]
        right =[1]

        # right = [len(nums)]
        # right[-1]=1
    
        for s in range(1,len(nums)):
            left.append(left[s-1]*nums[s-1])
            right.insert(0,right[-s]*nums[-s])
        
        for s in range(0,len(nums)):
            result.append(left[s]*right[s])

        return result
solution = Solution()
nums = [4,5,1,8,2,10,6]
print(solution.productExceptSelf(nums))
