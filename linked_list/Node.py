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
