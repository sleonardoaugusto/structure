class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
        else:
            temp = self.root
            while True:
                if value == temp.value:
                    return False
                if value < temp.value:
                    if not temp.left:
                        temp.left = node
                        return True
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = node
                        return True
                    temp = temp.right

    def contains(self, value):
        if not self.root:
            return False
        else:
            temp = self.root
            while temp:
                if value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
                else:
                    return True
            return False

    def minimum_value_node(self, node):
        while node.left:
            node = node.left
        return node
