# Linked Lists

See `py05_linked-list`

A linked list is a linear data structure where each element in a list is contained in a self-referential **node** object. 

Self-referential means nodes store a value (self), and a pointer to the next node (referential). Nodes also sometimes store a pointer to the previous node. The last node has no next pointer, which is how the language knows it's the end of the list.

The first node in a linked list is the **head**. The last node is the **tail**. The list only maintains a reference to the head (and sometimes tail) node - and not to every node. 

A node that stores just a next-node pointer is a **singly linked list**. A node that stores both a next-node and previous-node pointers is a **doubly linked list**.

