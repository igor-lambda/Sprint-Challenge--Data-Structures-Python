# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     """Wrap the given value in a ListNode and insert it
#     after this node. Note that this node could already
#     have a next node it is point to."""

#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     """Wrap the given value in a ListNode and insert it
#     before this node. Note that this node could already
#     have a previous node it is point to."""

#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     """Rearranges this ListNode's previous and next pointers
#     accordingly, effectively deleting this ListNode."""

#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev

#     def replace_with(self, new_node):
#         self.next.prev = new_node
#         new_node.next = self.next

# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""


# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         return self.length

#     def is_empty(self):
#         return self.length == 0

#     def increment_length(self):
#         self.length = self.length + 1

#     def decrement_length(self):
#         self.length = self.length - 1

#     """Wraps the given value in a ListNode and inserts it 
#     as the new head of the list. Don't forget to handle 
#     the old head node's previous pointer accordingly."""

#     def add_to_head(self, value):
#         new_node = ListNode(value)
#         if self.is_empty():
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.head.prev = new_node
#             new_node.next = self.head
#             self.head = new_node
#         self.increment_length()

#     def add_node_to_head(self, node):
#         if self.is_empty():
#             self.head = node
#             self.tail = node
#         else:
#             self.head.prev = node
#             node.next = self.head
#             self.head = node
#             self.increment_length()

#     """Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node."""

#     def remove_from_head(self):
#         if self.is_empty():
#             return None
#         elif self.length == 1:
#             value = self.head.value
#             self.head = None
#             self.tail = None
#             self.decrement_length()
#             return value
#         else:
#             value = self.head.value
#             self.head = self.head.next
#             self.head.prev = None
#             self.decrement_length()

#     """Wraps the given value in a ListNode and inserts it 
#     as the new tail of the list. Don't forget to handle 
#     the old tail node's next pointer accordingly."""

#     def add_to_tail(self, value):
#         new_node = ListNode(value)
#         if self.is_empty():
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.increment_length()

#     def add_node_to_tail(self, node):
#         if self.is_empty():
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             node.prev = self.tail
#             self.tail = node
#         self.increment_length()

#     """Removes the List's current tail node, making the 
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node."""

#     def remove_from_tail(self):
#         if self.is_empty():
#             return None
#         elif self.length == 1:
#             value = self.tail.value
#             self.head = None
#             self.tail = None
#             self.decrement_length()
#             return value
#         else:
#             value = self.tail.value
#             self.tail = self.tail.prev
#             self.tail.next = None
#             return value

#     """Removes the input node from its current spot in the 
#     List and inserts it as the new head node of the List."""

#     def move_to_front(self, node):
#         if self.is_empty() or self.head == node:
#             return None
#         else:
#             self.delete(node)
#             self.add_node_to_head(node)

#     """Removes the input node from its current spot in the 
#     List and inserts it as the new tail node of the List."""

#     def move_to_end(self, node):
#         if self.is_empty() or node == self.tail:
#             return None
#         else:
#             self.delete(node)
#             self.add_node_to_tail(node)

#     """Removes a node from the list and handles cases where
#     the node was the head or the tail"""

#     def delete(self, node):
#         if self.is_empty():
#             return None
#         elif self.length == 1:
#             if self.head == node:
#                 self.head = None
#                 self.tail = None
#         elif self.head == node:
#             self.head.next.prev = None
#             self.head = self.head.next
#         elif self.tail == node:
#             self.tail.prev.next = None
#             self.tail = node
#         else:
#             current_node = self.head.next
#             while current_node.next.next is not None:  # skipping head and tail nodes
#                 if current_node == node:
#                     current_node.prev.next = current_node.next
#                     current_node.next.prev = current_node.prev
#                 current_node = current_node.next
#         self.decrement_length()

#     """Returns the highest value currently in the list"""

#     def get_max(self):
#         if self.is_empty():
#             return None
#         elif self.length == 1:
#             return self.head.value
#         else:
#             max = self.head.value
#             current_node = self.head.next
#             while current_node is not None:
#                 if current_node.value > max:
#                     max = current_node.value
#                 current_node = current_node.next
#             return max

#     def replace(old, new):
#         old.



# class RingBuffer2:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.size = 0
#         self.store = DoublyLinkedList()
#         self.current = None
    
#     def at_capacity(self):
#         return self.size >= self.capacity

#     def increment_size(self):
#         self.size = self.size + 1

#     def decrement_size(self):
#         self.size = self.size - 1

#     def append(self, item):
#         if not self.at_capacity():
#             self.store.add_node_to_tail(ListNode(item))
#             self.increment_size()
#             if self.at_capacity():
#                 self.current = self.store.head
#         else:
            


#     def get(self):
#         pass

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.store = []
        self.current_index = 0
    
    def at_capacity(self):
        return self.size >= self.capacity

    def increment_size(self):
        self.size = self.size + 1

    def decrement_size(self):
        self.size = self.size - 1

    def append(self, item):
        if not self.at_capacity():
            self.store.append(item)
            self.increment_size()
        else:
            self.store[self.current_index] = item
            self.current_index = (self.current_index + 1) % self.capacity # modulo make sit start over after self.capacity

    def get(self):
        return self.store