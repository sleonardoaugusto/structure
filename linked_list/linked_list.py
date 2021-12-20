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
            self.tail = new_node
        else:
            self.tail.next = new_node
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
                self.tail = node.next
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
        node = self.head
        if node:
            self.head = node.next
            self.length -= 1
