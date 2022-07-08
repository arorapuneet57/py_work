class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None


    def insert_node(self, root):
        temp = self.head
        if self.head is None:
            self.head = root
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = root


    def create_loop_in_linked_list(self):
        current = self.head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = current

    def detect_and_delete_loop_in_linked_list(self):
        dic = {}
        count = 0
        temp = self.head
        while temp != None:
            dic[temp] = id(temp)
            current = temp
            temp = temp.next
            next_element_address = id(temp)
            if next_element_address in dic.values():
                print("\n Address values %s" % dic.values())
                print("\n Matched address %s" % next_element_address)
                current.next = None
                break

    def reverse_linked_list(self):
        temp = self.head
        current = temp
        prev = None
        while temp != None:
            temp = temp.next
            current.next = prev
            prev =  current
            current = temp
        self.head = prev


    def traverse_node(self):
        temp = self.head
        while temp is not None:
            print("   %s   " % temp.data, end="--")
            temp = temp.next


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
L1.create_loop_in_linked_list()
L1.detect_and_delete_loop_in_linked_list()
L1.traverse_node()
L1.reverse_linked_list()
L1.traverse_node()

