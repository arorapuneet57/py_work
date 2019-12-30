"""
   Tree traversal program
"""
import pdb;pdb.set_trace();
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Inorder(obj):
    current = obj
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current =  current.left
        elif(stack):
             current = stack.pop()
             print(current.data)
             current = current.right
        else:
             break
         




obj=Node(2)
obj.left=Node(1)
obj.right=Node(1)
obj.left.left=Node(10)
obj.right.right=Node(11)
obj.right.left=Node(-1)
Inorder(obj)



