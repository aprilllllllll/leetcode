class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea =0 

        left = 0
        right = len(height)-1

        while left<right:
            if height[left]> height[right]:
                h = height[right]
            else:
                h = height[left]

            w = right -left

            maxArea = max(maxArea,h*w)

            if height[left]> height[right]:
                right -=1
            else:
                left +=1


   

        return maxArea


solution = Solution()
height =[1,8,6,2,5,4,8,3,7]

print(solution.maxArea(height))
