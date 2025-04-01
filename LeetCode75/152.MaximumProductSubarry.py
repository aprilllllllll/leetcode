class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = 1
        min_product = 1
        result = float('-inf')
        for n in nums:
            curr = n

            if curr< 0:
                max_product,min_product= min_product,max_product
            
            max_product = max(max_product*curr,curr)
            min_product = min(min_product*curr,curr)
            result = max(result,max_product)
        
        return result

solution = Solution()
nums = [3,-1,4]
print(solution.maxProduct(nums))
