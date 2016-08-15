        tmp = Stack()
        while not stk.isEmpty():
            if not stk.isEmpty() and (tmp.isEmpty() or tmp.peek() >= stk.peek()):
                tmp.push(stk.peek())
                stk.pop()
            else:
                value = stk.peek()
                stk.pop()
                while not tmp.isEmpty() and tmp.peek() <= value:
                    stk.push(tmp.peek())
                    tmp.pop()

                stk.push(value);
                while not tmp.isEmpty():
                    stk.push(tmp.peek())
                    tmp.pop()

        while not tmp.isEmpty():
            stk.push(tmp.peek())
            tmp.pop()
