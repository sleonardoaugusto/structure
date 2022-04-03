from sorts.bubble_sort.bubble_sort import bubble_sort


def test_bubble_sort_three_items():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
