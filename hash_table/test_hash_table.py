from hash_table.hash_table import HashTable


def test_constructor():
    ht = HashTable()
    assert ht.data_map == [None] * 7


def test_set():
    ht = HashTable()
    ht.set('nuts', 10)
    assert ht.data_map == [None, None, None, None, None, None, [['nuts', 10]]]


def test_get_not_existent_item():
    ht = HashTable()
    assert ht.get('nuts') is None


def test_get_existent_item():
    ht = HashTable()
    ht.set('nuts', 10)
    assert ht.get('nuts') == 10


def test_keys_empty_hash_table():
    ht = HashTable()
    assert ht.keys() == []


def test_keys_not_empty_hash_table():
    ht = HashTable()
    ht.set('nuts', 10)
    ht.set('nails', 15)
    ht.set('bolts', 20)
    assert ht.keys() == ['bolts', 'nuts', 'nails']
