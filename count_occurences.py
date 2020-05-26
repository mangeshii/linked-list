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


    def count_occurences(self,data):
        count=0
        temp=self.head
        while temp:
            if temp.data == data:
                count += 1
            temp=temp.next
        return count



llist = Linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(1)
llist.append(6)
llist.append(1)
print(llist.count_dups(2))

llist.printlist()