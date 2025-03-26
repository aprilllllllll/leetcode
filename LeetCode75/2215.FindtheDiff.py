class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        return [list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))]

solution = Solution()
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]


print(solution.findDifference(nums1,nums2))