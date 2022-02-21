class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0
        self._create(value)

    def _create(self, value):
        node = Node(value)
        if value:
            self.head = node
            self.tail = node
            self.length += 1

    def append(self, value):
        if self.length == 0:
            self._create(value)
        else:
            node = Node(value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
