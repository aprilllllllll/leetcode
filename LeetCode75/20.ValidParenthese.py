class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket = {')':'(','}':'{',"]":"["}
        stack = []
        if len(s) % 2 != 0:
            return False
        else:
            for i in s:
                print(stack)
                if i in bracket.values():
                    stack.append(i)
                elif i in bracket.keys():
                    if bracket[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False

        return not stack 

solution = Solution()
s = "([)]"
print(solution.isValid(s))
