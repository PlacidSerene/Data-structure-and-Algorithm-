class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first == None:
            return None
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last  = new_node
        self.length += 1
    def printQueue(self):
        queue = []
        currentNode = self.first
        while (currentNode!= None):
            queue.append(currentNode.value)
            currentNode = currentNode.next
        return queue
    def dequeue(self):
        if self.length == 0:
            return "Nothing to remove"
        if self.length == 1:
            self.last = None
        self.first = self.first.next
        self.length -= 1
firstQueue = Queue()
firstQueue.enqueue(5)
firstQueue.enqueue(6)
firstQueue.enqueue(7)
print(firstQueue.printQueue())
firstQueue.dequeue()
print(firstQueue.printQueue())
firstQueue.dequeue()
print(firstQueue.printQueue())
firstQueue.dequeue()
print(firstQueue.printQueue())



        







