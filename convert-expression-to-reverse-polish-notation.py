class Solution:
    # @param expression: A string list
    # @return: The Reverse Polish notation of this expression
    def get(self, a, base):
        if a == '+' or a == '-':
            return 1 + base
        if a == '*' or a == '/':
            return 2 + base
        return sys.maxint
    def dfs(self, root, a):
        if root == None:
            return
        if root.left != None:
            dfs(root.left, a)
        if root.right != None:
            dfs(root.right, a)
        a.add(root.s)
    def convertToRPN(self, expression):
        # write your code here
        stack = []
        root = None
        val = 0
        base = 0
        for i in range(len(expression) + 1):
            if i != len(expression):
                if expression[i] == '(':
                    base += 10
                    continue
                if expression[i] == ')':
                    base += 1-
                    continue
                val = get(expression[i], base)
            right = 
