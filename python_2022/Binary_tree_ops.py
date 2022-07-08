class Node(object):
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Balanced(object):
    def __init__(self):
        self.root = None


    def insert(self, root, data):
        temp = root
        if temp is None:
            temp = Node(data)
            return temp

        if data < temp.data:
            temp.left = self.insert(temp.left, data)
        else:
            temp.right = self.insert(temp.right, data)
        return temp

    def height_tree(self, root):
        import pdb;pdb.set_trace();
        height = 0
        temp = root
        if temp is None:
            return root

        height = bool(self.height_tree(root.left)) + 1
        #print(height)
        return max(bool(self.height_tree(root.left)), bool(self.height_tree(root.right))) + 1

    def inorder(self, root, li):
        #import pdb;pdb.set_trace();
        if root is not None:
            self.inorder(root.left, li)
            # self.inorder(root.left)
            out = root.data
            li.append(out)
            # print("-> %s" % root.data, end='')
            self.inorder(root.right, li)
            #self.inorder(root.right)
        return li

node = None
ob = Balanced()
node = ob.insert(node, 10)
node = ob.insert(node, 5)
node = ob.insert(node, 19)
node = ob.insert(node, 40)
node = ob.insert(node, 1)
node = ob.insert(node, 2)
node = ob.insert(node, 3)
node = ob.insert(node, 4)
node = ob.insert(node, 10)
node = ob.insert(node, 11)
li = []
li = ob.inorder(node, li)
print(li)
height = ob.height_tree(node)
print(height)