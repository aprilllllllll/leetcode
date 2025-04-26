class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):return False
        if len(s) == 0:return True
        p=0
        for x in t:
            if s[p]== x:
                p+=1
            if p == len(s):
                return True
        return False

s = "abc"
t = "ahbgdc"

solution = Solution()
print(solution.isSubsequence(s,t))
