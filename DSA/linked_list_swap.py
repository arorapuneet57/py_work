from circular_linked_list import Node
from circular_linked_list import LinkedList


def swap_linked_list_link(head, x, y):
    temp = head
    prev = None
    while temp != None:
        if temp.data == x:
            prev1 = prev
            temp_node1 = temp
        if temp.data == y:
            prev2 = prev
            temp_node2 = temp

        prev = temp
        temp = temp.next

    if temp_node2.next is not None:
        check = temp_node2.next
    else:
        check = temp_node2
    if prev1 is not None:
        prev1.next = temp_node2
        temp_node2.next = temp_node1
        prev2.next = temp_node1
        temp_node1.next = check
    else:
        prev1 = check
        temp_node2.next = temp_node1.next
        prev2.next = temp_node1
        temp_node1.next = None
        head = temp_node2
        return head

def traverse_node(head):
    temp = head
    while temp is not None:
        print("   %s   " % temp.data, end="--")
        temp = temp.next

node1 = Node(10)
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(5)
L1 = LinkedList()

L1.insert_node(n1)
L1.insert_node(n2)
L1.insert_node(n3)
L1.insert_node(n4)
L1.traverse_node()
print("\n")
swap_linked_list_link(L1.head, 20, 30)
L1.traverse_node()
print("\n")
swap_linked_list_link(L1.head, 30, 20)
L1.traverse_node()
print("\n")
head = swap_linked_list_link(L1.head, 10, 5)
traverse_node(head)
