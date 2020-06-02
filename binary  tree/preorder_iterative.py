class Node:
    def __init__(self,data):
        self.data= data
        self.right=None
        self.left=None

def preorder_iterative(root):
    stack = [] # initialize the stack
    if root is None:
        return
    else:
        stack.append(root) # if my root node is not None then push it in the stack

    while len(stack) > 0:
        node=stack.pop()  
        print(node.data,end=" ")

        if node.right is not None: # if my right node is not None then push it in the stack
            stack.append(node.right)
        if node.left is not None:   # if my left node is not None then push it in the stack
            stack.append(node.left)



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

preorder_iterative(root)
