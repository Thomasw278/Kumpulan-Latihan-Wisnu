class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.isEmpty():
            return None
        popped_value = self.top_node.value
        self.top_node = self.top_node.next
        return popped_value

    def isEmpty(self):
        return self.top_node is None
