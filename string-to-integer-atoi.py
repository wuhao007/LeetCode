class Solution:
    # @return an integer
    def atoi(self, str):
        if str == '':
            return 0
        flag = ''
        result = 0
        for i in range(len(str)):
            if flag == '' and (str[i] == '-' or str[i] == '+'):
                flag = str[i]
            elif str[i] == ' ':
                continue
            elif str[i] < '0' or str[i] > '9':
                return 0
            else:
                result = result * 10 + (ord(str[i]) - ord('0'))
        if flag == '-':
            return -result
        else:
            return result
            
solution = Solution()
print solution.atoi("1")

