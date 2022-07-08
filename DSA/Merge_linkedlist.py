l1 = [2,5,7,9,15]
l2 = 3,6,11,13

#final = 2,3,5,6,7,9,11,13,15

class node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

pointer_head1 = LinkedList()
pointer_head2 = LinkedList()



pointer_head1.head = node(2)
second = node(5)
third = node(7)
fourth = node(9)
fifth = node(15)

pointer_head1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

pointer_head2.head = node(3)
a1 = node(6)
a2 = node(11)
a3 = node(13)

pointer_head2.head.next = a1
a1.next = a2
a2.next = a3

temp1 = pointer_head1.head
temp2 = pointer_head2.head
dummy_node = node(0)
dummy = dummy_node

"""
list1_count = 0
list2_count = 0

temp = temp1
while(temp is not None):
    list1_count += 1
    temp = temp.next

print("######")
temp = pointer_head2.head
while(temp is not None):
    list2_count += 1
    temp = temp.next

#for i in (0, list1_count + list2_count):
"""
while temp1 and temp2:
    try:
        if temp1.data > temp2.data:
            dummy.next = temp1
            temp1 = temp1.next
        if temp1.data < temp2.data:
            dummy.next = temp2
            temp2 = temp2.next
    except:
        pass
    dummy = dummy.next

final = dummy_node.next
while(final is not None):
    print(final.data)
    final = final.next

"""
address = []
address1 = []
for num in l1:
    address.append(Node(num))

for num in l2:
    address1.append(Node(num))



for num in address:
    if num.next is not None:
        num.next = 
    print(num.data)

print("###########")
for num in address1:
    print(num.data)
"""

