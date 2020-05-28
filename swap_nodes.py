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



    def swap_nodes(self, key_1, key_2):
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> none
        # 1 -> 3 -> 2 -> 4 -> 5 -> 6 -> 7 -> none

        if key_1 == key_2:
            return

        tempx = self.head
        prevx = None

        while tempx and tempx.data != key_1:
            prevx = tempx
            tempx = tempx.next

        #prevx = 1
        #tempx = 2
        #prevy = 2
        #tempy = 3

        tempy = self.head
        prevy = None

        while tempy and tempy.data != key_2:
            prevy = tempy
            tempy = tempy.next


        if prevx:
            prevx.next = tempy
        else:
            self.head = tempy

        if prevy:
            prevy.next = tempx
        else:
            self.head = tempx

        temporary = tempx.next
        tempx.next = tempy.next
        tempy.next = temporary


llist = Linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.append(7)

llist.swap_nodes(2,3)

llist.printlist()
