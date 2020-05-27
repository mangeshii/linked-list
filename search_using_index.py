class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


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
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode

    def search_position(self,index):
        temp=self.head
        count=0
        while temp is not None:
            if count == index:
                return temp.data
            count+=1
            temp=temp.next
       

llist = linkedlist()

llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

print(llist.search_position(3))


llist.printlist()
