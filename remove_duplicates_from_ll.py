class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


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

    def remove_dups(self):
        current = self.head

        while current.next is not None:
            if current.data == current.next.data:
                new = current.next.next
                current.next = None
                current.next = new
            else:
                current = current.next

llist = Linkedlist()
llist.append(1)
llist.append(1)
llist.append(1)
llist.append(1)
llist.append(2)
llist.append(7)
llist.append(5)
llist.append(6)

llist.remove_dups()


llist.printlist()
