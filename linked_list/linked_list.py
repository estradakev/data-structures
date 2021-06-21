class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert_node(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, nodeData):
        current = self.head
        itExists = False
        while current and itExists is False:
            if current.get_data() == nodeData:
                itExists = True
            else:
                current = current.get_next_node()
        if current is Node:
            raise ValueError("Data is not in the linked list")
        return current

    def size(self):
        current = self.head
        nodeCount = 0
        while current:
            nodeCount += 1
            current = current.get_next_node()
        return nodeCount

    def delete(self, nodeData):
        current = self.head
        previous = None
        itExists = False
        while itExists and current is False:
            if current.get_data() == nodeData:
                itExists = True
            else:
                previous = current
                current = current.get_next_node()
        if current is None:
            raise ValueError('Data is not in the linked list')
        if previous is None:
            self.head = current.get_next_node()
        else:
            previous.set_next(current.get_next_node())

    def list_print(self):
        current = self.head
        while current:
            self.size += 1
            print(str(current.data))
            current = current.get_next_node()


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # This method returns the data of the node
    def get_data(self):
        return self.data
    # This method returns the next node

    def get_next_node(self):
        return self.next_node

    # This method sets the next node
    def set_next(self, next_node):
        self.next_node = next_node


l = LinkedList()
n1 = Node('n1 info')
n2 = Node('n2 info')
n3 = Node('n3 info')
n4 = Node('n4 info')
n5 = Node('n5 info')
l.head = n1
l.head.next_node = n2
n2.next_node = n3
n3.next_node = n4
n4.next_node = n5
l.list_print()
