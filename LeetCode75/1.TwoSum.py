class Solution:
    def twoSum(self, nums, target):
        result =[]
        for i, num in enumerate(nums):
            x = target - num
            if(x in nums):
                y = nums.index(x)
                if y!=i:
                    return[i,y]
           
        return [] 

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))

