class Node(object):
    def __init__(self, val):
        self.data = val
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None

    def get_node(self, node_val):
        number = self.count_nodes()
        temp = self.head
        for num in range(0, number):
            if int(temp.data) == node_val:
                return temp
            else:
                if temp.next is not None:
                    temp = temp.next
                    continue
        print("node not found")

    def delete_all_nodes(self):
        current = self.head
        while current is not None:
            ahead = current.next
            del current.data
            current = ahead

    def insert_node(self, root):
        if self.head is None:
            self.head = root
        else:
            temp = self.head
            try:
                while temp.next != None:
                    temp = temp.next
                temp.next = root
            except:
                pass

    def delete_node(self, node_val):
        temp = self.head
        prev = temp
        if temp.data == node_val:
            self.head = temp.next
        else:
            while temp != None:
                if temp.data == node_val:
                    prev.next = temp.next
                    break
                prev = temp
                temp = temp.next


    def insert_at_desired_postion(self, position, root):
        number = self.count_nodes()
        temp = self.head
        for num in range(0, number):
            if num == position:
                temp1 = temp.next
                temp.next = root
                temp.next.next = temp1
            else:
                if temp.next is None:
                    temp.next = root
                    break
            temp = temp.next

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            count += 1
        return count

    def traverse_list(self):
        temp = self.head
        try:
            while temp != None:
                print("%s --> " % temp.data, end='')
                temp = temp.next
            print("\n")
        except:
            pass
        pass

root = Node(10)
root1 = Node(11)
root2 = Node(12)
root3 = Node(8)
L1 = Linked_list()
L1.insert_node(root)
L1.insert_node(root1)
L1.insert_node(root2)
L1.insert_node(root3)
L1.traverse_list()
root4 = Node(4)
L1.insert_at_desired_postion(1, root4)
root4 = Node(100)
L1.insert_at_desired_postion(0, root4)
root4 = Node(200)
L1.insert_at_desired_postion(100, root4)
L1.traverse_list()
print(" start delete 100")
L1.delete_node(100)
L1.traverse_list()
print(" start delete 200")
L1.delete_node(200)
L1.traverse_list()
print(" start delete 11")
L1.delete_node(11)
L1.traverse_list()
print(" start delete 10")
L1.delete_node(10)
L1.traverse_list()
node = L1.get_node(10)
try:
    print("Node found %s and its address %s" % (node.data, node))
except Exception as e:
    pass
node = L1.get_node(8)
try:
    print("Node found %s and its address %s" % (node.data, node))
except Exception as e:
    pass

L1.delete_all_nodes()
L1.traverse_list()

