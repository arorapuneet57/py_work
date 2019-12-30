class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        ins = self.head
        while ins.next:
            ins = ins.next
        ins.next = new_node

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    
    def traverse(self, k):
        count = 0
        temp = self.head
        while(temp):
            if (count+1) < k:
                 temp = temp.next
            else:
                temp.data = temp.next.data
                temp.next = temp.next.next
                break
    
            count += 1

     
val = [1,2,3,4,5]
li = LinkedList()
for i in val:
    li.insert(i)

#li.display()
import pdb;pdb.set_trace();
li.traverse(2)
li.display()
