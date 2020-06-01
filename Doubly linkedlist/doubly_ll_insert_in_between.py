class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
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

# 1->2->9->3->4->5
    def insert_in_between(self, prevnode, newdata):
        newnode = Node(newdata)
        if not prevnode:
            print('No such element in the list')
        else:
            nextnode = prevnode.next
            newnode.next = nextnode
            prevnode.next = newnode
            nextnode.prev = newnode
            newnode.prev = prevnode


llist = DoublyLinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

llist.insert_in_between(llist.head.next, 9)

llist.printlist()
