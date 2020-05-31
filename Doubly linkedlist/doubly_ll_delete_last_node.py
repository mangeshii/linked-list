class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = next
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def append(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = self.tail = newnode
            self.head.prev = None
            self.tail.next = None
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def delete_last(self):
        temp = self.tail
        if temp.next is None:
            # temp.prev=self.tail
            self.tail = temp.prev
            self.tail.next = None

llist = DoublyLinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

llist.delete_last()

llist.printlist()
