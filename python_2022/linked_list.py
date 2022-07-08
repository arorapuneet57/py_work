# Create single linked list

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

list = LinkedList()
list.head = Node(11)
second = Node(22)
third = Node(3)

list.head.next = second
second.next = third

# adding at the last location
temp = list.head
while(temp):
    if temp.next:
        temp = temp.next
        continue
    else:
        fourth = Node(4)
        third.next = fourth
        break

# traverse linked list
temp = list.head
while(temp):
    print(temp.data)
    temp = temp.next

print("$$$$$$$$$$$")
# Add node at the beganing
new_node = Node(100)
new_node.next = list.head
list.head = new_node

temp = list.head
while(temp):
    print(temp.data)
    temp = temp.next


print("$$$$$$$$$$$")
# reverse linked list
prev = None
current = list.head

while(current is not None):
    temp_pointer = current.next
    current.next = prev
    prev = current
    current = temp_pointer

list.head = prev

temp = list.head
while(temp):
    print(temp.data)
    temp = temp.next







