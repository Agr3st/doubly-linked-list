import pytest
from src.list import List, ElementNotFoundError


@pytest.fixture
def create_list() -> List:
    """Fixture to create a list with some initial values"""
    lst = List()
    lst.push('C')
    lst.push('B')
    lst.push('A')
    return lst


def test_push(create_list):
    lst = create_list
    assert lst.length == 3
    assert lst.head.data == 'A'
    assert lst.tail.data == 'C'


def test_pop(create_list):
    lst = create_list
    popped_node = lst.pop()
    assert popped_node.data == 'A'
    assert lst.length == 2
    assert lst.head.data == 'B'


def test_is_empty(create_list):
    lst = create_list
    assert not lst.is_empty()

    lst.pop()
    lst.pop()
    lst.pop()
    assert lst.is_empty()


def test_append(create_list):
    lst = create_list
    lst.append('D')
    assert lst.tail.data == 'D'
    assert lst.length == 4


def test_insert(create_list):
    lst = create_list

    # test insertion at the beginning
    lst.insert('D', 0)
    assert lst.head.data == 'D'
    assert lst.length == 4

    # test insertion between two elements
    lst.insert('E', 2)
    assert lst._get_node(2).data == 'E'
    assert lst._get_node(3).data == 'B'
    assert lst.length == 5

    # test insertion at the end
    lst.insert('F', 5)
    assert lst._get_node(lst.length).data == 'F'
    assert lst.length == 6

    # test invalid index
    with pytest.raises(IndexError):
        lst.insert('G', 10)


def test_delete(create_list):
    lst = create_list

    # test deleting an element between two elements
    lst.delete(1)
    assert lst.length == 2
    assert lst._get_node(0).data == 'A'
    assert lst._get_node(2).data == 'C'

    # test deleting first element
    lst.delete(0)
    assert lst.length == 1
    assert lst.head.data == 'C'

    # test invalid index
    with pytest.raises(IndexError):
        lst.delete(5)

    # test deleting last element
    lst.delete(0)
    assert lst.is_empty()

    # test when list is empty
    with pytest.raises(IndexError):
        lst.delete(0)


def test_find_first_index(create_list):
    lst = create_list
    index = lst.find_first_index('C')
    assert index == 2

    # test invalid start index
    with pytest.raises(ValueError):
        lst.find_first_index('C', 5)

    # test element not found
    with pytest.raises(ElementNotFoundError):
        lst.find_first_index('X', 0)


def test_find_all_indexes(create_list):
    lst = create_list
    lst.push('B')
    indexes = lst.find_all_indexes('B')
    assert indexes == [0, 2]

    # test finding indexes for non-existent elements
    indexes = lst.find_all_indexes('X')
    assert indexes == []


def test_display(create_list, capsys):
    lst = create_list
    lst.display()
    captured = capsys.readouterr()
    assert "0: A <====> 1: B <====> 2: C" in captured.out
    assert "List length: 3" in captured.out
