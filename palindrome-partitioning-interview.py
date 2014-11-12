class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        def isPalindrome(s):
            beg = 0
            end = len(s) - 1
            while beg < end:
                if s[beg] != s[end]:
                    return False
                beg += 1
                end -= 1
            return True
        def helper(s, path, pos, result):
            if pos == len(s):
                result += path[:]
            else:
                for i in range(pos + 1, len(s) + 1):
                    prefix = s[pos:i]
                    if isPalindrome(prefix):
                        path += [prefix]
                        helper(s, path, i, result)
                        path.pop()
        result = []
        helper(s, [], 0, result)
        return sorted(set(result))
solution = Solution()
print solution.partition('aab') == ['a', 'aa', 'b']
print solution.partition('ACCABBA') == ['A', 'ABBA', 'ACCA', 'B', 'BB', 'C', 'CC']
