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

    def reverse(self):
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6  -> 7 -> none
        # 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> none
        prev=None
        current=self.head

        while current:
            temp=current.next
            current.next=prev  
            prev=current 
            current=temp
           
        self.head=prev
        
            
        


llist = Linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.append(7)
llist.reverse()

llist.printlist()
