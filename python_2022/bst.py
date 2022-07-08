class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Operations(object):
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        if self.root is None:
            self.root = Node(5)
        else:
            temp = self.root
            while temp is not None:
                prev = temp
                if data > temp.data:
                    temp = temp.right
                else:
                    temp = temp.left
            if data > prev.data:
                prev.right = Node(data)
            else:
                prev.left = Node(data)

    def traversal_node(self, root):
        temp = root
        if temp is not None:
            self.traversal_node(temp.left)
            print("-> %s" % temp.data, end=' ')
            self.traversal_node(temp.right)

    def insert_bst_with_recurrsion(self, temp, data):
        if temp is None:
            temp = Node(data)
            return temp

        if data > temp.data:
            temp.right = self.insert_bst_with_recurrsion(temp.right, data)
        else:
            temp.left = self.insert_bst_with_recurrsion(temp.left, data)
        return temp

    def inorder(self, root):
        if root is not None:
            import pdb;pdb.set_trace();
            self.inorder(root.left)
            print("--> %s" % root.data, end=" ")
            self.inorder(root.right)


op = Operations()
"""
op.insert_node(10)
op.insert_node(40)
op.insert_node(20)
op.insert_node(8)

op.insert_node(12)
op.insert_node(100)
op.insert_node(1)
op.insert_node(3)

op.traversal_node(op.root)
"""
print("\n")
node = None
node = op.insert_bst_with_recurrsion(node, 5)
node = op.insert_bst_with_recurrsion(node, 10)
node = op.insert_bst_with_recurrsion(node, 2)
node = op.insert_bst_with_recurrsion(node, 20)
node = op.insert_bst_with_recurrsion(node, 15)
op.inorder(node)