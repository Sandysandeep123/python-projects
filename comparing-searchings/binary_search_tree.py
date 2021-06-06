class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert(self, data, node):
        if node is None:
            node = Node(data)
        else:
            if data > node.data:
                if node.right is None:
                    node.right = Node(data)
                else:
                    self.__insert(data, node.right)
            elif data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self.__insert(data, node.left)

    def __search(self, data, node):
        if node:
            if data == node.data:
                return node
            else:
                if data < node.data:
                    return self.__search(data, node.left)
                else:
                    return self.__search(data, node.right)
        return None

    def __printing_in_order(self, node):
        if node:
            self.__printing_in_order(node.left)
            print(node.data)
            self.__printing_in_order(node.right)

    def __printing_pre_order(self, node):
        if node:
            print(node.data)
            self.__printing_pre_order(node.left)
            self.__printing_pre_order(node.right)

    def __printing_post_order(self, node):
        if node:
            self.__printing_post_order(node.left)
            self.__printing_post_order(node.right)
            print(node.data)

    def insert(self, data):
        if self.root:
            self.__insert(data, self.root)
        else:
            self.root = Node(data)

    def search(self, data):
        return self.__search(data, self.root)

    def printing_in_order(self):
        if self.root:
            self.__printing_in_order(self.root)

    def printing_pre_order(self):
        if self.root:
            self.__printing_pre_order(self.root)

    def printing_post_order(self):
        if self.root:
            self.__printing_post_order(self.root)
