class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        def simplifyPath(path, stack):
            if path == []:
                return '/' + '/'.join(stack)
            elif path[0] == '' or path[0] == '.':
                return simplifyPath(path[1:], stack)
            elif path[0] == '..':
                if stack != []:
                    stack.pop()
                return simplifyPath(path[1:], stack)
            else:
                stack += [path[0]]
                return simplifyPath(path[1:], stack)
        return simplifyPath(path.split('/'), [])
solution = Solution()
print solution.simplifyPath('/home/')
print solution.simplifyPath('/a/./b/../../c/')
print solution.simplifyPath('/..')
