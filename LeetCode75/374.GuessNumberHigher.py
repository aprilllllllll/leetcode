pick =2
n = 2

def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (guess(n)==0):
            return n

        mini = 1
        maxm = n
        x = int((mini+maxm)/2)

        while guess(x)!=0:
            if guess(x)==-1:
                maxm =x
                x = x = (mini+maxm)/2
            elif guess(x)==1:
                mini =x
                x = x = (mini+maxm)/2
        return x

solution = Solution()
print(solution.guessNumber(pick))