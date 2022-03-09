class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value=None):
        self.first = None
        self.last = None
        self.length = 0
        self._create(value)

    def _create(self, value):
        if value:
            node = Node(value)
            self.first = node
            self.last = node
            self.length = 1

    def enqueue(self, value):
        if not self.length:
            self._create(value)
        else:
            node = Node(value)
            self.last.next = node
            self.last = node
            self.length += 1

    def dequeue(self):
        if not self.length:
            raise IndexError
        elif self.length == 1:
            self.first = None
            self.last = None
            self.length = 0
        else:
            self.first = self.first.next
            self.length -= 1
