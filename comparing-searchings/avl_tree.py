class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def __init__(self):
        self.root = None

    def __insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.data:
            node.left = self.__insert(node.left, key)
        else:
            node.right = self.__insert(node.right, key)

        node.height = 1 + max(self.__getHeight(node.left),
                              self.__getHeight(node.right))

        balance = self.__getBalance(node)
        # ll
        if balance > 1 and key < node.left.data:
            return self.__rightRotate(node)

        # rr
        if balance < -1 and key > node.right.data:
            return self.__leftRotate(node)

        # lr
        if balance > 1 and key > node.left.data:
            node.left = self.__leftRotate(node.left)
            return self.__rightRotate(node)

        # rl
        if balance < -1 and key < node.right.data:
            node.right = self.__rightRotate(node.right)
            return self.__leftRotate(node)

        return node

    def __leftRotate(self, z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2

        z.height = 1 + max(self.__getHeight(z.left),
                           self.__getHeight(z.right))
        y.height = 1 + max(self.__getHeight(y.left),
                           self.__getHeight(y.right))
        return y

    def __rightRotate(self, z):

        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.__getHeight(z.left),
                           self.__getHeight(z.right))
        y.height = 1 + max(self.__getHeight(y.left),
                           self.__getHeight(y.right))
        return y

    def __getHeight(self, node):
        if not node:
            return 0

        return node.height

    def __getBalance(self, node):
        if not node:
            return 0

        return self.__getHeight(node.left) - self.__getHeight(node.right)

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

    def insert(self, key):
        self.root = self.__insert(self.root, key)

    def search(self, data):
        return self.__search(data, self.root)
