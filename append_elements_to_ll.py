class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self): 
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next


    def append(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while lastnode.next is not None:
            lastnode=lastnode.next
        lastnode.next=newnode


llist=Linkedlist()
llist.append(1)
llist.append(2)   

llist.printlist()  