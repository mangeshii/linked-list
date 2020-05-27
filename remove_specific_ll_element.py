# 1->2->3->4->5->6
# val = 5
# 1->2->3->4->6


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode

        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode

    def remove(self, value):
        temp = self.head
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next

            if temp.data == value:
                prev.next = temp.next


llist = linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist.remove(5)

llist.printlist()
