class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):  # why does this method exist?
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if not self.head:
            return
        if not node.get_next(): # we've reached the last node, make it new head
            self.head = node
            node.set_next(prev)
        else:    
            next = node.get_next() # if not at the end, we simplu preserve a referece to next,
            node.set_next(prev) # and switch the current node's next for the previous node
            self.reverse_list(next, node) # call reverse_list with next node for node, and current for previous
