class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        result=[]
        
        for i in range(len(flowerbed)):
            print(flowerbed)
            if n ==0 : break
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1

        if n!=0: return False
        else: return True

solution = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(solution.canPlaceFlowers(flowerbed,n))
