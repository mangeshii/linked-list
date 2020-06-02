class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.tail = newnode
            self.head.prev = None
            self.tail.next = None
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode


    def pop(self):
        if self.tail.prev is None:
            self.head = None
        if self.head is None:
            print('list is empty')
        else:
            prev = self.tail.prev
            self.tail = prev
            prev.next = None



llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

llist.pop()
llist.pop()
llist.pop()
llist.pop()
llist.pop()
llist.pop()


llist.printlist()
