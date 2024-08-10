from list import List

if __name__ == '__main__':
    # creating a list
    linked_list = List()

    # pushing first node
    print("Pushing first element to the list:")
    linked_list.push('1_element')
    linked_list.display()
    print()

    # pushing second node
    print("Pushing second element to the list:")
    linked_list.push('2_element')
    linked_list.display()
    print()

    # pushing three more nodes
    print("Pushing three more elements to the list:")
    linked_list.push('3_element')
    linked_list.push('4_element')
    linked_list.push('5_element')
    linked_list.display()
    print()

    # popping first element
    print("Popping first element from the list:")
    popped_element = linked_list.pop()
    print(f"Popped element: {popped_element}")
    linked_list.display()
    print()

    # inserting new element
    print("Inserting new element at position 1 (where 3_element was):")
    linked_list.insert('6_element', 1)
    linked_list.display()
    print()

    # adding new element at the end of the list
    print("Adding new element at the end of the list:")
    linked_list.append('7_element')
    linked_list.display()
    print()

    # deleting an element
    print("Deleting the element at position 2 (3_element):")
    linked_list.delete(2)
    linked_list.display()
    print()

    # deleting an element
    print("Deleting the element at position 0 (4_element):")
    linked_list.delete(0)
    linked_list.display()
    print()

    # deleting an element
    print("Deleting the element at position 3 (7_element):")
    linked_list.delete(3)
    linked_list.display()
    print()

    # searching for the element
    print("Searching for the 2_element")
    found_index = linked_list.get_first_index('2_element')
    print(f'Found index: {found_index}')
    print()

    # adding three more nodes
    print("Adding three more elements to the list:")
    linked_list.push('8_element')
    linked_list.push('8_element')
    linked_list.insert('8_element', 5)
    linked_list.display()
    print()

    # searching for all occurrences
    print("Searching for all occurrences of the 8_element")
    found_index = linked_list.get_all_index('8_element')
    print(f'Found indexes: {found_index}')
