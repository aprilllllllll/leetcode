class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k == 1: return max(nums)

        max_sum = temp = sum(nums[:k])
        for x in range(k,len(nums)):
            temp = temp -nums[x-k]+nums[x]
            if temp > max_sum:
                max_sum = temp

        return float(max_sum)/k
