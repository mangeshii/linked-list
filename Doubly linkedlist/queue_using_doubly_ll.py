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

    def prepend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.tail = newnode
            self.head.prev = None
            self.tail.next = None
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.tail.prev is None:
            self.head=None
        if self.head is None:
            print('list is empty')
        else:
            prev = self.tail.prev
            self.tail = prev
            prev.next = None



llist = LinkedList()
llist.prepend(1)
llist.prepend(2)
llist.prepend(3)
llist.prepend(4)

llist.pop()
llist.pop()
llist.pop()



llist.printlist()
