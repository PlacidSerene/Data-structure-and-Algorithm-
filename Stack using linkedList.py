class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.length >= 1:
            return self.top.value
        else:
            return None
    def push(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.bottom = new_node
            self.top = self.bottom

        else:
            holding_point = self.top
            self.top = new_node
            self.top.next = holding_point
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.bottom = None    
        self.top = self.top.next
        self.length -= 1
firstStack = Stack()
firstStack.push('google')
firstStack.push('facebook')
firstStack.push('amazon')
firstStack.push('netflix')
print(firstStack.peek())
firstStack.pop()
firstStack.pop()
firstStack.pop()
firstStack.pop()
print(firstStack.bottom)




        







