class Stack:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()
firstStack = Stack()
firstStack.push('google')
firstStack.push('facebook')
firstStack.push('amazon')
firstStack.push('netflix')
print(firstStack.peek())
firstStack.pop()
print(firstStack.stack)



        







