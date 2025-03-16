class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        i = 0
        idx = 0
        while i < n:
            ch = chars[i]
            count = 0
            print(chars[i], " ", count, idx)
            while i < n and chars[i] == ch:
                count += 1
                i += 1
            if count == 1:
                chars[idx] = ch
                idx += 1
            else:
                print(ch)
                chars[idx] = ch
                idx += 1

                for digit in str(count):
                    chars[idx] = digit
                    idx += 1
        chars[:] = chars[:idx]
        return idx


chars = ["a", "a", "b", "b", "c", "c", "c"]
solution = Solution()
print(solution.compress(chars))
