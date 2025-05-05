class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        lowprice =float('inf')
        for p in prices:

            lowprice = min(lowprice,p)

            maxProfit = max(maxProfit, p-lowprice)
        
        return maxProfit

solution = Solution()
prices =[2,4,1]

print(solution.maxProfit(prices))
