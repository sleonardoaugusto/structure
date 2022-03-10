import pytest

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


def test_pop_empty_list():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.pop()


def test_pop_length_1():
    dll = DoublyLinkedList(1)
    dll.pop()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0


def test_pop_length_2():
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.pop()
    assert dll.head.value == 1
    assert dll.head.next is None
    assert dll.tail.value == 1
    assert dll.length == 1


def test_prepend_empty_list():
    dll = DoublyLinkedList()
    dll.prepend(1)
    assert dll.head.value == 1
    assert dll.tail.value == 1
    assert dll.length == 1


def test_prepend_length_1():
    dll = DoublyLinkedList(1)
    dll.prepend(2)
    assert dll.head.value == 2
    assert dll.head.next.value == 1
    assert dll.tail.value == 1
    assert dll.tail.prev.value == 2
    assert dll.length == 2


def test_pop_first_empty_list():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.pop_first()


def test_pop_first_length_1():
    dll = DoublyLinkedList(1)
    dll.pop_first()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0


def test_pop_first_length_2():
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.pop_first()
    assert dll.head.value == 2
    assert dll.tail.value == 2
    assert dll.length == 1


def test_get_empty_list():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.get(0)


def test_get():
    dll = DoublyLinkedList(1)
    assert dll.get(0).value == 1


def test_set_empty_list():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.set(1, 0)


def test_set_length_1():
    dll = DoublyLinkedList(1)
    dll.set(2, 0)
    assert dll.head.value == 2


def test_insert_empty_list():
    dll = DoublyLinkedList()
    dll.insert(1, 0)
    assert dll.head.value == 1
    assert dll.tail.value == 1
    assert dll.length == 1


def test_insert_on_the_beginning():
    dll = DoublyLinkedList(2)
    dll.insert(1, 0)
    assert dll.head.value == 1
    assert dll.tail.value == 2
    assert dll.length == 2


def test_insert_on_the_middle():
    dll = DoublyLinkedList(1)
    dll.append(3)
    dll.insert(2, 1)
    assert dll.head.value == 1
    assert dll.head.next.value == 2
    assert dll.head.next.prev == dll.head
    assert dll.tail.prev == dll.head.next
    assert dll.tail.value == 3
    assert dll.length == 3


def test_insert_on_the_end():
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.insert(3, 2)
    assert dll.head.value == 1
    assert dll.head.next.value == 2
    assert dll.head.next.prev == dll.head
    assert dll.tail.prev == dll.head.next
    assert dll.tail.value == 3
    assert dll.length == 3


def test_remove_empty_list():
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.remove(0)


def test_remove_on_the_beginning():
    dll = DoublyLinkedList(1)
    dll.remove(0)
    assert dll.head is None
    assert dll.tail is None
    assert dll.length == 0


def test_remove_on_the_middle():
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    dll.remove(1)
    assert dll.head.value == 1
    assert dll.head.next == dll.tail
    assert dll.tail.value == 3
    assert dll.tail.prev == dll.head
    assert dll.length == 2
