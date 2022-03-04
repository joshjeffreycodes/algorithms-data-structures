# -------------------------------
# Linked Lists
# -------------------------------
class Node(): 
  '''A self-referentail node object for
  use in a singly linked list. Stores
  data + a pointer to next node. 
  '''
  data = None
  next_node = None
  # previous_node = None

  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return '<Node data: %s>' % self.data


class LinkedList:
  '''Constructs a singly linked list of nodes.
  The newest node becomes the `head` of the list.  
  ```
  nato = LinkedList()
  nato.is_empty()
  nato.size()
  nato.prepend(data)
  nato.insert(data, index)
  nato.remove_index(data, index)
  nato.remove_key(key)
  ```
  '''
  def __init__(self): 

    self.head = None

  def __repr__(self):
    '''Returns a string represtnation of the linked list.
    * Linear time.
    '''
    nodes = []
    current = self.head

    while current:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.next_node == None:
        nodes.append("[Tail: %s]" % current.data)
      else:
        nodes.append("[Node: %s]" % current.data)
      
      current = current.next_node

    return ' -> '.join(nodes)

  def is_empty(self):
    '''Returns bool. `True` if linked list is empty.
    '''
    return self.head == None

  def size(self): 
    '''Returns the number of nodes in a linked list. 
    * Linear time. 
    '''
    current = self.head
    count = 0

    while current: 
      count += 1 
      current = current.next_node
    
    return count

  def prepend(self,data):
    '''Prepends node to start of the linked list.
    * Constant time
    '''
    # The new node becomes the new list head,
    # and points to the old head. 
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

  def search(self,key):
    '''Searches the linked list for the 
    FIRST node containg data that matches the key.
    * Linear time. 
    * Returns the node or `None`
    '''
    current = self.head

    while current:
      if current.data == key:
        return current
      else:
        current = current.next_node
      
    return None

  def insert(self,data,index):
    '''Inserts node into the linked list at the
    given index position.
    * Linear time - finding the insertion point
    * Constant time - inserting the node
    * TODO: IndexError handling
    '''
    if index == 0:
      self.prepend(data)
    
    if index > 0:
      new = Node(data)
      position = index
      current = self.head

      # Above we deal with [0]. 
      # Implied here is that if the index is [1],
      # we are already where we need to be. 

      # This while loop is for indexes [2]+. 
      # It finds the node that is currently at the index
      # where we want to put the new node. 
      # It keeps track by counting backwards from the index number. 
      while position > 1:
        current = current.next_node
        position -= 1

      # The new node needs to go where the current node is. 
      # This works because above we counted backwards from the index as if 
      # it were an integer / counter, and not an index - so we wind up 
      # in the right postion. 

      # To 'move' the current node, we need to update its pointers
      # to reflect its new position. 

      # The current node becomes the new node's previous node.  
      node_previous = current
      # The current node's next node become the new node. 
      node_previous.next_node = new
      # The current node's next node becomes the new node's next node. 
      node_next = current.next_node 
      new.next_node = node_next

  def remove_key(self,key):
    '''Removes node with the given key
    (data / value) from the linked list.
    * Linear time.
    * Returns the node that was deleted or `None`
    '''
    current = self.head
    previous = None
    found = False 

    # `found` is a negator. 
    # It's used as a double-negative in `while`.
    while current and not found:
      # If the head node has the key, remove it
      # and make the 2nd node the new head. 
      if current.data == key and current == self.head:
        found = True
        self.head = current.next_node
      # To remove a node that is not the head, 
      # We simply point its next and previous nodes at 
      # each other - reomiving the middleman. 
      elif current.data == key:
        found = True
        previous.next_node = current.next_node
      # If we reach this case, no matching key is found
      else:
        previous = current
        current = current.next_node
    # It's common for remove commands to return
    # the reomved node. 
    return current

  def remove_index(self,index):
    '''Removes node with the given index
    from the linked list.
    '''
    # TODO

  def read_index(self,index):
    '''Reads and returns the value at 
    a given index
    '''
    # TODO

# -------------------------------
# Use
# -------------------------------
n1 = Node(2)
n1.data = 7
print(n1)

# nato = LinkedList()
# nato.prepend('alpaha')
# nato.prepend('bravo')
# nato.prepend('delta')
# print(nato)

# nato.insert('charlie',1)
# print(nato)