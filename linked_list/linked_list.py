class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = None
        self._create(value)

    def _create(self, value):
        if value is None:
            self.length = 0
        else:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length = 1

    def print_list(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        node = self.head
        while node:
            if node.next is None:
                self.head = None
                self.tail = None
                self.length = 0
                break
            elif node.next.next is None:
                node.next = None
                self.tail = node
                self.length -= 1
                break
            node = node.next

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        temp = self.head
        if temp:
            self.head = temp.next
        self.length -= 1
        if self.length == 0:
            self.tail = None

    def get(self, idx):
        temp = self.head
        for _ in range(idx):
            temp = temp.next
        return temp

    def set_value(self, idx, value):
        temp = self.get(idx)
        temp.value = value

    def insert(self, idx, value):
        if idx < 0 or idx > self.length:
            raise IndexOutOfRange
        elif idx == 0:
            self.prepend(value)
        elif idx == self.length:
            self.append(value)
        else:
            node = Node(value)
            temp = self.head
            for _ in range(idx - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
            self.length += 1

    def remove(self, idx):
        if idx < 0 or idx > self.length - 1:
            raise IndexOutOfRange
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


class IndexOutOfRange(BaseException):
    ...
