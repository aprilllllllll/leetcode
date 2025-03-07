class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):return False
        if len(s) == 0:return True

        subsequence=0
        for i in range(0,len(t)):
            print(subsequence)
            if subsequence < len(s):
                print(s[subsequence])
                if s[subsequence]==t[i]:

                    subsequence+=1
        return  subsequence == len(s)         

s = "abc"
t = "ahbgdc"

solution = Solution()
print(solution.isSubsequence(s,t))
