class Solution:
    def twoSum(self, nums, target):
        result =[]
        for i, num in enumerate(nums):
            x = target - num
            if(x in nums):
                y = nums.index(x)
                if y!=i:
                    return[i,y]
           

        return []  # Return an empty list if no valid pair is found


# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
