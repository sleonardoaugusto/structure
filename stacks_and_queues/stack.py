class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value=None):
        self.top = None
        self.height = 0
        self._create(value)

    def _create(self, value):
        if value:
            node = Node(value)
            self.top = node
            self.height += 1

    def push(self, value):
        if value:
            if self.height:
                node = Node(value)
                node.next = self.top
                self.top = node
                self.height += 1
            else:
                self._create(value)

    def pop(self):
        if not self.height:
            raise IndexError
        elif self.height == 1:
            self.top = None
            self.height = 0
        else:
            temp = self.top.next
            self.top = temp
            self.height -= 1
