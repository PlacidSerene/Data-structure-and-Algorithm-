# class myLinkedList:
#     def __init__(self):
#         head = {
#             value: 10,
#             next: {
#                 value: 5,
#                 next{
#                     value: 16,
#                     next: None
#                 }
#             }
#         }
class myLinkedList:
    def __init__(self, value):
        self.head = {    
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1
    def append(self,item):
        newNode = {
            'value': item,
            'next': None
        }
        newNode = Node(5)
        self.tail['next'] = newNode
        self.tail = newNode 
        self.length += 1
    def prepend(self,item):
        newNode = {
            'value': item,
            'next': self.head
        }
        self.head = newNode
        self.length += 1

class Node:
    def __init__(self,value):
        self = {
           "value": value,
            "next": None
        }

# firstLinkedList = myLinkedList(15)
# firstLinkedList.append(5)
# firstLinkedList.append(10)
# firstLinkedList.prepend(8)
# print(firstLinkedList.head)
# print(firstLinkedList.tail)
# print(firstLinkedList.length)
newNode = Node(5)
print(newNode)

