# data-structures

This section is about implementation of data structures, I write notes about how fast they are and code them .

### Linked Lists

* To be able to implement the linked lists I first had to implement a node class
* This consisted of
  * initialized method containing **<u>self.data</u>** and <u>**self.next_node**</u>
  * The other methods that are needed in the node class are getters for **<u>node_data</u>** and **<u>next_node</u>**
  * The last method needed for the node class is <u>**set_next**</u> (setting a new node) with a parameter of a node

* After the node class is implemented the linked_list class will be created

* It consists of the following:

  * insert
    * the method will be inserting a new node inside the linked list
  * search
    * returns the data of the given node if not found it will print an error
  * delete
    * deletes the node in the linked list if it is not found it will be giving an error
  * size
    * returns the size of the linked list

  