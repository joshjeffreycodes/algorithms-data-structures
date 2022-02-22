# Data Structures

## Learning Objectives

* Answer: Why we need more data structures than a programming language provides?
* Arrays - How they work, common operations, and associated runtimes.
* Build a linked list data structure - Explore some of the many ways data can be stored. 
* Answer: What motivates us to build certain structures?
* Explore the pros and cons of various structures by looking at 4 common operations. 
* Implement a sorting algorithm on 2 different data structures. 
* Learn how the choice of data structure can impact an algorithm's runtime.
* Learn about 'divide and conquer' - a key algorithmic thinking concept.

## What is a data structure?

A **data structure** describes how data is stored and formatted. How input is structured **impacts the space complexity** of an algorithm. A data structure includes: 

* The collection of values.
* The format values are stored in.
* The relationship between values in a collection.
* The operations applied on the data stored in the structure. 

All data structures are expected to carry out 4 operations: 

* Access and read values from the structure
* Search for an arbitrary value in the structure
* Insert values at any point into the structure
* Delete values from the structure. 

All programing languages provide data structures, so why do we need additional structures, why would we create our own? 

This section explores data structures and space complexity by looking at arrays and linked lists in Python. 

## Why build data structures?

...instead of using ones built in to the programing language? The short answer is, because each structure solves a particular problem. For example, arrays are good at accessing values (constant time), but less efficient with search, add, and delete (linear time). Linked lists are somewhat better at these things, but with caveats. 


