class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0
        self._create(value)

    def _create(self, value):
        if value:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length += 1

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def pop(self):
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length > 1:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def pop_first(self):
        if self.length:
            temp = self.head
            self.head = temp.next
            if self.length == 1:
                self.tail = None

            self.length -= 1

    def get(self, idx):
        if idx >= self.length or idx < 0:
            raise IndexError

        temp = self.head
        for _ in range(idx):
            temp = temp.next
        return temp

    def set_value(self, idx, value):
        temp = self.get(idx)
        temp.value = value

    def insert(self, idx, value):
        if idx == 0:
            self.prepend(value)
        elif idx == self.length:
            self.append(value)
        else:
            temp = self.head
            for _ in range(idx - 1):
                temp = temp.next
            node = Node(value)
            node.next = temp.next
            temp.next = node
            self.length += 1

    def remove(self, idx):
        if idx < 0 or idx > self.length or not self.length:
            raise IndexError

        elif idx == 0:
            self.pop_first()
        elif idx == self.length - 1:
            self.pop()
        else:
            temp = self.head
            for _ in range(idx - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.length -= 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
