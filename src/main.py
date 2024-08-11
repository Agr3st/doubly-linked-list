from list import List, ElementNotFoundError

if __name__ == '__main__':
    # creating a list
    linked_list = List()

    # pushing first node
    print("Pushing first element to the list:")
    linked_list.push('A')
    linked_list.display()
    print()

    # pushing second node
    print("Pushing second element to the list:")
    linked_list.push('B')
    linked_list.display()
    print()

    # pushing three more nodes
    print("Pushing three more elements to the list:")
    linked_list.push('C')
    linked_list.push('D')
    linked_list.push('E')
    linked_list.display()
    print()

    # popping first element
    print("Popping first element from the list:")
    popped_element = linked_list.pop()
    print(f"Popped element: {popped_element}")
    linked_list.display()
    print()

    # inserting new element
    print("Inserting new element at position 1 (where C was):")
    linked_list.insert('F', 1)
    linked_list.display()
    print()

    # adding new element at the end of the list
    print("Adding new element at the end of the list:")
    linked_list.append('G')
    linked_list.display()
    print()

    # deleting an element
    print("Deleting the element at position 2 (C):")
    linked_list.delete(2)
    linked_list.display()
    print()

    # deleting an element
    print("Deleting the element at position 0 (D):")
    linked_list.delete(0)
    linked_list.display()
    print()

    # deleting an element
    print("Deleting the element at position 3 (G):")
    linked_list.delete(3)
    linked_list.display()
    print()

    # searching for the element
    print("Searching for the B")
    found_index = linked_list.find_first_index('B')
    print(f'Found index: {found_index}')
    print()

    # adding three more nodes
    print("Adding three more elements to the list:")
    linked_list.push('H')
    linked_list.push('H')
    linked_list.insert('H', 4)
    linked_list.display()
    print()

    # searching for all occurrences
    print("Searching for all occurrences of the H")
    found_index = linked_list.find_all_indexes('H')
    print(f'Found indexes: {found_index}')
