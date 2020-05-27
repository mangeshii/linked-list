
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
        lastnode = self.head
        while lastnode.next is not None:
            lastnode = lastnode.next
        lastnode.next = newnode

    def insert_in_between(self,prev_node,newdata):
        newnode=Node(newdata)
        if not prev_node:
            print('previous node is not in the list')
        else:
            newnode.next=prev_node.next
            prev_node.next=newnode


llist = Linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.insert_in_between(llist.head.next.next,7)


llist.printlist()
