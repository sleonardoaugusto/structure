import pytest

from stacks_and_queues.stack import Stack


def test_constructor_empty_stack():
    s = Stack()
    assert s.top is None
    assert s.height == 0


def test_constructor():
    s = Stack(1)
    assert s.top.value == 1
    assert s.height == 1


def test_push_empty_list():
    s = Stack()
    s.push(1)
    assert s.top.value == 1
    assert s.height == 1


def test_push():
    s = Stack(1)
    s.push(2)
    assert s.top.value == 2
    assert s.top.next.value == 1
    assert s.height == 2


def test_pop_empty_list():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_pop_height_1():
    s = Stack(1)
    s.pop()
    assert s.top is None
    assert s.height == 0


def test_pop_height_2():
    s = Stack(1)
    s.push(2)
    s.pop()
    assert s.top.value == 1
    assert s.height == 1
