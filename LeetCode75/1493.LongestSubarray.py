class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        prev = 0  # Stores the count of previous segment of 1s
        curr = 0  # Stores the count of current segment of 1s
        for num in nums:
            if num == 1:
                curr += 1  # Increment current segment count
            else:

                max_length = max(max_length, prev + curr)  # Consider merging previous and current segments
                print(prev,curr,max_length)
                prev= curr  # Move current count to previous for next iteration
                curr = 0  # Reset current count
        
        # Final check in case we never encountered a zero
        max_length = max(max_length, prev + curr)
        if(curr == len(nums)):
            return max_length-1
        else:
   

            return max_length


nums =[1,1,0,0,1,1,1,0,1]
solution = Solution()
print(solution.longestSubarray(nums))