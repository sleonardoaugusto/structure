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

    def prepend(self, value):
        if self.length == 0:
            self._create(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.length += 1

    def pop_first(self):
        if self.length == 0:
            raise IndexError
        elif self.length == 1:
            self.pop()
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

    def get(self, idx):
        if self.length == 0:
            raise IndexError
        temp = self.head
        for _ in range(idx):
            temp = temp.next
        return temp

    def set(self, value, idx):
        temp = self.get(idx)
        temp.value = value
