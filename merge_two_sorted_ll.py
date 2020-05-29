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

    def merge(self, llist):
        p = llist1.head
        q = llist2.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p



llist1 = linkedlist()

llist1.append(1)
llist1.append(4)
llist1.append(6)
llist1.append(7)

llist2 = linkedlist()

llist2.append(2)
llist2.append(3)
llist2.append(5)
llist2.append(8)

llist1.merge(llist2)

llist1.printlist()
