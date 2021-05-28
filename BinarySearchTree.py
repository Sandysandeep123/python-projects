class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert(self, data, node):
        if node is None:
            node = Node(data)
        else:
            if data > node.data:
                if node.right_child is None:
                    node.right_child = Node(data)
                else:
                    self.__insert(data, node.right_child)
            elif data < node.data:
                if node.left_child is None:
                    node.left_child = Node(data)
                else:
                    self.__insert(data, node.left_child)

    def __search(self, data, node):
        if node:
            if data == node.data:
                return node
            else:
                if data < node.data:
                    return self.__search(data, node.left_child)
                else:
                    return self.__search(data, node.right_child)
        return None

    def __printing_in_order(self, node):
        if node:
            self.__printing_in_order(node.left_child)
            print(node.data)
            self.__printing_in_order(node.right_child)

    def __printing_pre_order(self, node):
        if node:
            print(node.data)
            self.__printing_pre_order(node.left_child)
            self.__printing_pre_order(node.right_child)

    def __printing_post_order(self, node):
        if node:
            self.__printing_post_order(node.left_child)
            self.__printing_post_order(node.right_child)
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
