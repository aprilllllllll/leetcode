class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count =0
        l = {}


        for num in nums:
            r = k-num
            if r in l and l[r]>0:
                count+=1
                l[r]-=1
            else:
                if num in l:
                    l[num]+=1
                else:
                    l[num]=1



        return count

        
solution = Solution()

nums = [3,5,1,5]
k = 2

print(solution.maxOperations(nums,k))