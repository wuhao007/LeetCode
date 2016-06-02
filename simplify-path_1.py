class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk = []
        for tmp in path.split('/'):
            if tmp == '' or tmp == '.':
                continue
            if tmp == '..' and stk:
                stk.pop()
            elif tmp != '..':
                stk.append(tmp)
        return '/' + '/'.join(stk)
