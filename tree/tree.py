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
