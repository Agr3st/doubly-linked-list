from typing import Any


class ElementNotFoundError(Exception):
    """Exception raised when an element is not found in the list."""


class _ListNode:
    def __init__(self, data: Any):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.
        :return: True if empty, False otherwise
        """
        return self.head is None

    def push(self, data: Any) -> None:
        """
        Create and add an element at the beginning of the list.
        :param data: data to be in list node
        """
        new_node = _ListNode(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def pop(self) -> _ListNode:
        """
        Pop the first element from the beginning.
        :return: popped list node
        """
        # 0 nodes
        if self.is_empty():
            raise IndexError("The list is empty.")

        node_to_pop = self.head
        # 1 node
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # 2 or more nodes
        else:
            self.head = node_to_pop.next
            self.head.prev = None

        self.length -= 1
        return node_to_pop

    def append(self, data) -> None:
        """
        Append a node with data at the end of the list
        :param data: data to be stored in list node
        """
        if self.is_empty():
            self.push(data)
            return

        new_node = _ListNode(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def insert(self, data: Any, position: int) -> None:
        """
        Insert a node with data at specific position in the list (index from 0).
        :param data: data to be stored in list node
        :param position: new node's index
        :raises IndexError: if position is out of range.
        """
        if position < 0 or position > self.length:
            raise IndexError("Position out of range.")

        if position == 0:
            self.push(data)
            return

        previous_node = self._get_node(position - 1)
        if previous_node is self.tail:
            self.append(data)
        else:
            new_node = _ListNode(data)
            new_node.next = previous_node.next
            new_node.prev = previous_node
            previous_node.next.prev = new_node
            previous_node.next = new_node
            self.length += 1

    def delete(self, position: int) -> None:
        """
        Delete a list node from the specific position.
        :param position: element's index (from 0)
        :raises IndexError: if the list is empty or the position is out of range.
        """
        if self.is_empty():
            raise IndexError("Cannot delete an element from an empty list.")
        if position < 0 or position >= self.length:
            raise IndexError("Position out of range.")

        node_to_delete = self._get_node(position)

        if node_to_delete is self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        del node_to_delete
        self.length -= 1

    def find_first_index(self, data: Any, start_index: int = 0) -> int:
        """
        Returns an index of the first occurrence of the list node with specific data.
        :param start_index: index of element from which to start searching
        :param data: data stored in the list node
        :return: index of the list node
        :raises ValueError: if start_index is invalid
        :raises ElementNotFoundError: if element not found
        """
        if not self._is_valid_index(start_index) or self.is_empty():
            raise ValueError("Invalid start index")

        current_node = self._get_node(start_index)
        current_index = start_index
        while current_node:
            if current_node.data == data:
                return current_index
            current_node = current_node.next
            current_index += 1

        raise ElementNotFoundError(f"Element {data} not found in the list.")

    def find_all_indexes(self, data: Any) -> list[int]:
        """
        Returns an index of the first occurrence of the list node with specific data.
        :param data: data stored in the list node
        :return: list of indexes of the list nodes
        """
        found_indexes = []
        current_index = 0

        while current_index < self.length:
            try:
                result = self.find_first_index(data, start_index=current_index)
            except ElementNotFoundError:
                break
            else:
                found_indexes.append(result)
                current_index = result + 1

        return found_indexes

    def display(self) -> None:
        """
        Display the list (index: data), and list length.
        """
        current_node = self.head
        current_index = 0
        while current_node:
            print(f' {current_index}: {current_node} ', end="")
            if current_index >= 0 and current_node.next is not None:
                print("<====>", end="")
            current_node = current_node.next
            current_index += 1
        print(f'\nList length: {self.length}')

    def _get_node(self, position: int) -> _ListNode:
        """
        Returns list node from the specific position.
        :param position: element's index (from 0)
        :return: list node
        """
        if position <= (self.length - 1 - position):
            current_index = 0
            current_node = self.head
            while current_node and current_index < position:
                current_node = current_node.next
                current_index += 1
        else:
            current_index = self.length - 1
            current_node = self.tail
            while current_node and current_index > position:
                current_node = current_node.prev
                current_index -= 1
        return current_node

    def _is_valid_index(self, index: int) -> bool:
        """
        Checks if the given index is within the bounds of the list.
        :param index: index to check
        :return: True if valid, False otherwise
        """
        return 0 <= index < self.length
