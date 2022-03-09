import pytest

from stacks_and_queues.queue import Queue


def test_constructor_empty():
    q = Queue()
    assert q.first is None
    assert q.last is None
    assert q.length == 0


def test_constructor():
    q = Queue(1)
    assert q.first.value == 1
    assert q.last.value == 1
    assert q.length == 1


def test_enqueue_without_length():
    q = Queue()
    q.enqueue(1)
    assert q.first.value == 1
    assert q.last.value == 1
    assert q.length == 1


def test_enqueue_with_length():
    q = Queue(1)
    q.enqueue(2)
    assert q.first.value == 1
    assert q.last.value == 2
    assert q.length == 2


def test_dequeue_without_length():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_dequeue_with_length_1():
    q = Queue(1)
    q.dequeue()
    assert q.first is None
    assert q.last is None
    assert q.length == 0


def test_dequeue_with_length_2():
    q = Queue(1)
    q.enqueue(2)
    q.dequeue()
    assert q.first.value == 2
    assert q.last.value == 2
    assert q.length == 1
