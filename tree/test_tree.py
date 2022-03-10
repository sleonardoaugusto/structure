from tree.tree import BinarySearchTree


def test_constructor():
    t = BinarySearchTree()
    assert t.root is None


def test_should_insert_on_the_root():
    t = BinarySearchTree()
    t.insert(1)
    assert t.root.value == 1


def test_should_insert_on_the_right():
    t = BinarySearchTree()
    t.insert(1)
    t.insert(2)
    assert t.root.right.value == 2


def test_should_insert_on_the_left():
    t = BinarySearchTree()
    t.insert(2)
    t.insert(1)
    assert t.root.left.value == 1


def test_should_return_false_if_value_already_exists():
    t = BinarySearchTree()
    t.insert(1)
    assert t.insert(1) is False
