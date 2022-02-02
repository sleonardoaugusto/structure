import pytest

from linked_list.linked_list import LinkedList, IndexOutOfRange


def test_init():
    """Should init with node"""
    linked_list = LinkedList(2)
    assert linked_list.length == 1
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 2


def test_init_without_value():
    """Should init without node"""
    linked_list = LinkedList()
    assert linked_list.length == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_append():
    """Should append node"""
    linked_list = LinkedList()
    linked_list.append(2)
    assert linked_list.length == 1
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 2


def test_append_without_node():
    linked_list = LinkedList(1)
    linked_list.append(2)
    assert linked_list.length == 2
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 2


def test_pop_with_one_node():
    """Should remove the only node"""
    linked_list = LinkedList(1)
    linked_list.pop()
    assert linked_list.length == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_pop_with_two_nodes():
    """Should remove last node"""
    linked_list = LinkedList(2)
    linked_list.append(3)
    linked_list.pop()
    assert linked_list.length == 1
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 2


def test_prepend_without_length():
    """Should add node if list is empty"""
    linked_list = LinkedList()
    linked_list.prepend(2)
    assert linked_list.length == 1
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 2


def test_prepend():
    """Should add node if list is not empty"""
    linked_list = LinkedList(2)
    linked_list.prepend(3)
    assert linked_list.length == 2
    assert linked_list.head.value == 3
    assert linked_list.tail.value == 2


def test_pop_first_without_length():
    """Should remove the only node"""
    linked_list = LinkedList(1)
    linked_list.pop_first()
    assert linked_list.length == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_pop_first():
    """Should remove first node"""
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.pop_first()
    assert linked_list.length == 1
    assert linked_list.head.value == 2
    assert linked_list.tail.value == 2


def test_get_index():
    """Should return value by index"""
    linked_list = LinkedList(1)
    assert linked_list.get(0).value == 1


def test_set_value():
    """Should set new value by index"""
    linked_list = LinkedList(1)
    linked_list.set_value(0, 2)
    assert linked_list.head.value == 2


def test_insert_out_of_range():
    """Should raise an exception if index is out of range"""
    linked_list = LinkedList(1)
    with pytest.raises(IndexOutOfRange):
        linked_list.insert(2, 2)


def test_insert_on_the_head():
    """Should insert item on the top of the list"""
    linked_list = LinkedList(1)
    linked_list.insert(0, 2)
    assert linked_list.get(0).value == 2
    assert linked_list.head.value == 2


def test_insert_on_the_middle():
    """Should insert item on the middle of the list"""
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.insert(1, 3)
    assert linked_list.get(1).value == 3
    assert linked_list.get(1).next.value == 2


def test_insert_on_the_end():
    """Should insert item on the end of the list"""
    linked_list = LinkedList(1)
    linked_list.insert(1, 2)
    assert linked_list.get(1).value == 2
    assert linked_list.tail.value == 2


def test_remove_out_of_range():
    """Should raise an exception if index is out of range"""
    linked_list = LinkedList(1)
    with pytest.raises(IndexOutOfRange):
        linked_list.remove(1)


def test_remove_on_the_head():
    """Should remove item by index on head"""
    linked_list = LinkedList(1)
    linked_list.remove(0)
    assert linked_list.get(0) is None
    assert linked_list.head is None
    assert linked_list.tail is None


def test_remove_on_the_middle():
    """Should remove item by index on middle"""
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.remove(1)
    assert linked_list.get(0).value == 1
    assert linked_list.get(1).value == 3


def test_remove_on_the_end():
    """Should remove item by index on end"""
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.remove(1)
    assert linked_list.get(0).value == 1
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
