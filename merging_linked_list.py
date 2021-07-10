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


def merge_linked_lists(linked_list_1, linked_list_2):
    listFinal = LinkedList()
    head1 = linked_list_1.head
    head2 = linked_list_2.head
    tempNode = Node(0)
    start = tempNode
    while 1:
        if head1 is None:
            start.next = head2
            break
        if head2 is None:
            start.next = head1
            break
        if head1.data <= head2.data:
            start.next = head1
            head1 = head1.next
        else:
            start.next = head2
            head2 = head2.next
        start = start.next
    listFinal.head = tempNode.next
    return listFinal


if __name__ == '__main__':
    listOne = LinkedList()
    listTwo = LinkedList()

    listOne.add_at_head(Node(16))
    listOne.add_at_head(Node(10))
    listOne.add_at_head(Node(5))

    listTwo.add_at_head(Node(14))
    listTwo.add_at_head(Node(11))
    listTwo.add_at_head(Node(6))
    a = merge_linked_lists(listOne, listTwo)
    a.print_list()
    a.print_backward()
