class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def append(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            return
        else:
            lastnode = self.head

        while lastnode.next is not None:
            lastnode = lastnode.next
        lastnode.next = newnode

    def swap_tail(self):
        temp = self.head
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next
        temp.next = self.head
        self.head = temp
        prev.next = None
        return


llist = Linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(10)
llist.swap_tail()

llist.printlist()
