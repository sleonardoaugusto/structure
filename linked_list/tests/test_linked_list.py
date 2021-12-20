from linked_list.linked_list import LinkedList, Node


def test_init():
    """Should init with node"""
    linked_list = LinkedList(2)
    assert linked_list.length == 1
    assert isinstance(linked_list.head, Node)
    assert isinstance(linked_list.tail, Node)


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
    assert isinstance(linked_list.head, Node)
    assert isinstance(linked_list.tail, Node)


def test_pop_with_one_node():
    """Should remove the only node"""
    linked_list = LinkedList(1)
    linked_list.pop()
    assert linked_list.length == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_pop_with_two_nodes():
    """Should remove last node"""
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.pop()
    assert linked_list.length == 1
    assert isinstance(linked_list.head, Node)
    assert isinstance(linked_list.tail, Node)


def test_prepend_without_length():
    """Should add node if list is empty"""
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.length == 1
    assert isinstance(linked_list.head, Node)
    assert isinstance(linked_list.tail, Node)


def test_prepend():
    """Should add node if list is not empty"""
    linked_list = LinkedList(1)
    linked_list.prepend(2)
    assert linked_list.length == 1
    assert isinstance(linked_list.head, Node)
    assert isinstance(linked_list.tail, Node)


def test_pop_first_without_length():
    """Should remove the only node"""
    linked_list = LinkedList()
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
    assert isinstance(linked_list.head, Node)
    assert isinstance(linked_list.tail, Node)
