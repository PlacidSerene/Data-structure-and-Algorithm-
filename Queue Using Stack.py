class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []



    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        a = self.stack1.pop()

        return a
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1[len(self.stack1)-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0

queue1 = MyQueue()
queue1.push('google')
queue1.push('facebook')
queue1.push('amazon')
print(queue1.peek())
print(queue1.pop())
