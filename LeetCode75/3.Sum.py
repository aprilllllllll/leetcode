class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]== nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left <right:
            

                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while nums[left-1] == nums[left] and left<right:
                        left+=1

                elif sum <0:
                    left+=1
                else:
                    res.append([nums,nums[left],nums[right]])
                    left+=1
                


        return res

solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))
