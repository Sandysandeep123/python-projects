class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __addData(self, data, node):
        if node is None:
            node = Node(data)
        else:
            if data > node.data:
                if node.right_child is None:
                    node.right_child = Node(data)
                else:
                    self.__addData(data, node.right_child)
            elif data < node.data:
                if node.left_child is None:
                    node.left_child = Node(data)
                else:
                    self.__addData(data, node.left_child)

    def addData(self, data):
        if self.root:
            self.__addData(data, self.root)
        else:
            self.root = Node(data)


bst = BinarySearchTree()
bst.addData(5)
bst.addData(3)
bst.addData(2)
bst.addData(8)
