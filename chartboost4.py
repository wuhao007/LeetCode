from sys import stdin, stdout
userinput = stdin.readline()
def isValid(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack += [c]
        elif c == ')' and (len(stack) == 0 or stack.pop() != '('):
            return False
        elif c == ']' and (len(stack) == 0 or stack.pop() != '['):
            return False
        elif c == '}' and (len(stack) == 0 or stack.pop() != '{'):
            return False
    return len(stack) == 0
if isValid(userinput):
    stdout.write("Valid")
else:
    stdout.write("Not Valid")
