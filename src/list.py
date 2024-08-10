from typing import Any


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
        Pop the first element from the return it.
        :return: popped list node
        """
        # 0 nodes
        if self.is_empty():
            return None

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

        new_node = _ListNode(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def insert(self, data: Any, position: int) -> bool:
        """
        Insert a node with data at specific position in the list (index from 0).
        :param data: data to be stored in list node
        :param position: new node's index
        :return: True if success, else False
        """
        if position < 0 or position > self.length:
            return False

        if position == 0:
            self.push(data)
            return True

        previous_node = self._get_node(position - 1)
        if previous_node is self.tail:
            self.append(data)
        else:
            next_node = self._get_node(position)
            new_node = _ListNode(data)

            previous_node.next = new_node
            new_node.prev = previous_node

            next_node.prev = new_node
            new_node.next = next_node

            self.length += 1

        return True

    def delete(self, position: int) -> bool:
        """
        Delete a list node from the specific position.
        :param position: element's index (from 0)
        :return: True if success, False if failure
        """
        if self.is_empty() or position < 0 or position >= self.length:
            return False

        node_to_delete = self._get_node(position)
        # node to be deleted is the only node in list
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        # 2+ nodes in the list and the one to be deleted is the first one
        elif node_to_delete is self.head:
            self.head = node_to_delete.next
            self.head.prev = None
        # 2+ nodes in the list and the one to be deleted is the last one
        elif node_to_delete is self.tail:
            self.tail = node_to_delete.prev
            self.tail.next = None
        # 3+ nodes in the list and the one to be deleted is between others
        else:
            # node_to_delete.prev.next = node_to_delete.next
            # node_to_delete.next.prev = node_to_delete.prev
            previous_node = self._get_node(position - 1)
            next_node = self._get_node(position + 1)

            previous_node.next = next_node
            next_node.prev = previous_node

        del node_to_delete
        self.length -= 1
        return True

    def display(self) -> None:
        """
        Display the list (index: data), and list length.
        """
        current_node = self.head
        current_index = 0
        while current_node:
            print(f'{current_index}: {current_node}')
            current_node = current_node.next
            current_index += 1
        print(f'List length: {self.length}')

    def get_first_index(self, data: Any, start_index: int = 0) -> int:
        """
        Returns an index of the first occurrence of the list node with specific data.
        :param start_index: index of element from which to start searching
        :param data: data stored in the list node
        :return: index of the list node, -1 if not found
        """
        if not self._is_valid_index(start_index):
            return -1  # zmienic na wyjatek

        current_node = self._get_node(start_index)
        current_index = start_index
        while current_node:
            if current_node.data == data:
                return current_index
            current_node = current_node.next
            current_index += 1

    def get_all_index(self, data: Any) -> [int]:
        """
        Returns an index of the first occurrence of the list node with specific data.
        :param data: data stored in the list node
        :return: list of indexes of the list nodes, -1 if not found
        """
        found_indexes = []
        current_index = 0
        result = 0

        while result != -1:
            result = self.get_first_index(data, start_index=current_index)
            if result != -1:
                found_indexes.append(result)
            current_index = result + 1
        return found_indexes

    def _get_node(self, position: int) -> _ListNode:
        current_node = self.head
        current_index = 0
        while current_node and current_index < position:
            current_node = current_node.next
            current_index += 1
        return current_node

    def _is_valid_index(self, index):
        return 0 <= index < self.length
