class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        def palindrome(elem):
            n = len(elem)
            for i in range(n/2):
                if elem[i] != elem[n-1-i]:
                    return False
            return True
        result = [[s[0]]]
        for i in range(1,len(s)):
            ch = s[i]
            n = len(result)
            for j in range(n):
                if palindrome(result[j][-1]):
                    new_element = result[j][:]
                    new_element += [ch]
                    result += [new_element]
                result[j][-1] += ch
        palindrome_result = []
        for lst in result:
            is_palindrome = True
            for elem in lst:
                if palindrome(elem) == False:
                    is_palindrome = False
                    break;
            if is_palindrome:
                palindrome_result += [lst]
        return palindrome_result
solution = Solution()
print solution.partition('aab')
