class Bag:
    """Linked List implementation of Bag data structure"""

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, item):
        curr_node = self._head
        while curr_node is not None and curr_node.data != item:
            curr_node = curr_node.next
        return curr_node is not None

    def add(self, item):
        """Add item at the head of the list"""
        new_node = _BagListNode(item)
        new_node.next = self._head
        self._head = new_node
        print(new_node)

    def remove(self, item):
        """Remove item from the list"""

        # search from the start of the linked-list and keep a pointer to the prev-node
        prev_node = None
        curr_node = self._head

        while curr_node is not None and curr_node.data != item:
            # item is not in the curr_node. So, search the next node
            prev_node = curr_node
            curr_node = curr_node.next

        # raise an assert error if item is not found
        assert curr_node is not None, f"Item [{item}] not found"

        # remove the current node by adjusting pointers
        # if the curr-node is HEAD then make proper pointer adjustments
        if curr_node is self._head:
            self._head = curr_node.next
        else:
            prev_node.next = curr_node.next

        # reduce the size of the bag since the item has been removed
        self._size -= 1

        return f"Removed [{curr_node.data}]"

    def __iter__(self):
        return _BagIterator(self._head)


class _BagListNode:
    def __init__(self, item):
        self.data = item
        self.next = None

    def __repr__(self):
        return f"{self.data} -> {self.next}"


class _BagIterator:
    def __init__(self, head):
        self.head = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            raise StopIteration


if __name__ == "__main__":
    input_items = list(input("Enter items in the bag: ").split())
    bag = Bag()
    for item in input_items:
        bag.add(item)

    for x in bag:
        print(x)
