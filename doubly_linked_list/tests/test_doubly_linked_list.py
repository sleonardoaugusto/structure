from doubly_linked_list.doubly_linked_list import DoublyLinkedList


def test_constructor_without_value():
    dll = DoublyLinkedList()
    assert dll.length == 0
    assert dll.head is None
    assert dll.tail is None


def test_constructor():
    dll = DoublyLinkedList(1)
    assert dll.length == 1
    assert dll.head.value == 1
    assert dll.tail.value == 1


def test_append_empty_list():
    dll = DoublyLinkedList()
    dll.append(1)
    assert dll.length == 1
    assert dll.head.value == 1
    assert dll.head.next is None
    assert dll.tail.value == 1
    assert dll.tail.next is None


def test_append():
    dll = DoublyLinkedList(1)
    dll.append(2)
    assert dll.length == 2
    assert dll.head.value == 1
    assert dll.head.next.value == 2
    assert dll.tail.value == 2
    assert dll.tail.prev.value == 1
