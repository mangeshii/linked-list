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

  
       
    def palindrome(self,string):
        return string==string[::-1]


    def merge(self):
        head1=llist.head
        head2=llist2.head   
        while head1.next is not None:
            head1=head1.next
        if head1.next is None:
            head1.next=head2
        
        



llist = Linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

llist2=Linkedlist()
llist2.append(6)
llist2.append(7)
llist2.append(8)
llist2.append(9)
llist.merge()



llist.printlist()


