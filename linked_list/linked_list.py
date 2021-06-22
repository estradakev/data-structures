class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    # The method inserts a node at the begining of the
    def insert_node(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # The method takes in the data of the node and serches it through the list
    def search(self, nodeData):
        current = self.head
        itExists = False
        while current and itExists is False:
            if current.get_data() == nodeData:
                itExists = True
            else:
                current = current.get_next_node()
        if current is None:
            print("Data is not in the linked list")
        return current

    # This returns the size of the list
    def size_of_list(self):
        current = self.head
        nodeCount = 0
        while current:
            nodeCount += 1
            current = current.get_next_node()
        return nodeCount

    def delete_node(self, nodeData):
        current = self.head
        previous = None
        itExists = False
        while itExists is False and current:
            if current.get_data() == nodeData:
                itExists = True
            else:
                previous = current
                current = current.get_next_node()
        if current is None:
            raise ValueError('Data is not in the linked list\n')
        if previous is None:
            self.head = current.get_next_node()
        else:
            previous.set_next(current.get_next_node())

    # This method traverses through the list and prints the values of the nodes
    def list_print(self):
        current = self.head
        while current:
            self.size += 1
            print(str(current.get_data()))
            current = current.get_next_node()


# This is a class that wil be representing a node for the linked list
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


# creating the nodes
my_list = LinkedList()
n1 = Node('n1 info')
n2 = Node('n2 info')
n3 = Node('n3 info')
n4 = Node('n4 info')
n5 = Node('n5 info')

# adding nodes to the list
my_list.head = n1
my_list.head.next_node = n2
n2.next_node = n3
n3.next_node = n4
n4.next_node = n5
my_list.list_print()
print('\n')
my_list.insert_node("n6 info")
my_list.insert_node("n7 info")
my_list.list_print()

my_list.delete_node('n4 info')
my_list.delete_node('n2 info')

my_list.search('n8')

sizeOfList = my_list.size_of_list()
print('\nsize of the list is ' + str(sizeOfList) + '\n')

my_list.list_print()
