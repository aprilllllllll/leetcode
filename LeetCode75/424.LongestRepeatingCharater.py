from turtle import right


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        max_len=0
        l=0
        seen ={}
        maxFreq = 0
        for r in range(len(s)):
            if s[r] in seen:
                seen[s[r]]+=1

            else:
                seen[s[r]]=1
            maxFreq = max(maxFreq,seen[s[r]])

            while (r-l+1) - maxFreq >k:
                seen[s[l]] -=1
                l+=1

            max_len = max(max_len,r-l+1)
        return max_len
solution = Solution()

s="ABAB"
k=2


print(solution.characterReplacement(s,k))