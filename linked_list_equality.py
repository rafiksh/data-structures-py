class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_list(self):
        node = self.head
        while node is not None:
            print(node, end=' ')
            node = node.next
        print('')

    def add_at_head(self, node):
        node.next = self.head
        self.head = node
        self.length += 1

    def remove_node_after(self, node):
        if node.next is not None:
            temp = node.next
            node.next = node.next.next
            temp.next = None
            self.length -= 1

    def remove_first_node(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

    def print_backward(self):
        def print_nodes_backward(node):
            if node.next is not None:
                print_nodes_backward(node.next)
            if node is not None:
                print(node, end=' ')

        if self.head is not None:
            print_nodes_backward(self.head)

        print('')


def equal_linked_lists(linked_list_1, linked_list_2):
    one = linked_list_1.head
    two = linked_list_2.head
    while one is not None and two is not None:
        if one.data != two.data:
            return False
        else:
            one = one.next
            two = two.next
    return one == two


if __name__ == '__main__':

    print(equal_linked_lists('sds'))
