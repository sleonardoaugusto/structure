import pytest

from linked_list.linked_list import LinkedList


def test_constructor():
    ll = LinkedList(1)
    assert ll.head.value == 1
    assert ll.tail.value == 1
    assert ll.head.next is None
    assert ll.length == 1


def test_constructor_empty_value():
    ll = LinkedList()
    assert ll.head is None
    assert ll.tail is None
    assert ll.length == 0


def test_append():
    ll = LinkedList(1)
    ll.append(2)
    assert ll.head.value == 1
    assert ll.tail.value == 2
    assert ll.head.next.value == 2
    assert ll.length == 2


def test_pop_with_one_item():
    ll = LinkedList(1)
    ll.pop()
    assert ll.head is None
    assert ll.tail is None
    assert ll.length == 0


def test_pop_with_two_items():
    ll = LinkedList(1)
    ll.append(2)
    ll.pop()
    assert ll.head.value == 1
    assert ll.tail.value == 1
    assert ll.head.next is None
    assert ll.length == 1


def test_prepend():
    ll = LinkedList(2)
    ll.prepend(1)
    assert ll.head.value == 1
    assert ll.tail.value == 2
    assert ll.length == 2
    assert ll.head.next.value == 2


def test_get():
    ll = LinkedList(1)
    node = ll.get(0)
    assert node.value == 1


def test_get_out_of_range():
    ll = LinkedList(1)
    with pytest.raises(IndexError):
        ll.get(1)


def test_set_value():
    ll = LinkedList(1)
    ll.set_value(0, 2)
    assert ll.get(0).value == 2


def test_insert_on_the_beginning():
    ll = LinkedList(2)
    ll.insert(0, 1)
    assert ll.head.value == 1
    assert ll.tail.value == 2
    assert ll.head.next.value == 2
    assert ll.length == 2


def test_insert_on_the_middle():
    ll = LinkedList(1)
    ll.append(3)
    ll.insert(1, 2)
    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 3
    assert ll.length == 3


def test_insert_on_the_end():
    ll = LinkedList(1)
    ll.append(2)
    ll.insert(2, 3)
    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 3
    assert ll.tail.value == 3
    assert ll.length == 3


def test_remove_out_of_range():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.remove(0)


def test_remove_from_the_beginning():
    ll = LinkedList(1)
    ll.remove(0)
    assert ll.head is None
    assert ll.tail is None
    assert ll.length == 0


def test_remove_from_the_middle():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.remove(1)
    assert ll.head.value == 1
    assert ll.head.next.value == 3
    assert ll.tail.value == 3
    assert ll.length == 2


def test_remove_from_the_end():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.remove(2)
    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.tail.value == 2
    assert ll.length == 2


def test_reverse():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.reverse()
    assert ll.head.value == 3
    assert ll.head.next.value == 2
    assert ll.tail.value == 1
    assert ll.length == 3
