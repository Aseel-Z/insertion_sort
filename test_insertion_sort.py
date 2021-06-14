from insertion_sort import InsertionSort

def test_InsertionSort():
    arr = [8,4,23,42,16,15]
    actual = InsertionSort(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

