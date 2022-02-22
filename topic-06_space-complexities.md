# Topic 6: Space Complexities

Recall that an algorithm can be described by its time and space complexities. At this point we've explored time complexity via Big O runtimes. Now we turn to how Big O describes **space complexity** - a worst-case measure of how much additional memory an algorithm needs as the value of ***n*** grows.

## O(1) - Constant Space - Linear & Iterative Binary Search

With linear search and iterative binary search, we use a `for` loop to iterate over values in a single list. Once this list is in memory, it's size does not change as the size of ***n*** changes - hence these have **constant space** complexities. 

## O(log n) - Logarithmic Space - Recursive Binary Search

A **recursive function** is a function that calls itself. It continues to call itself until it has a concrete answer or the stop condition is met. Then it returns the answer back up the chain to the original function. 

Recursive binary search works by splitting a list in half. It discards one of the two lists, then calls itself again using the other list. 

In other words, with each guess we create a new list - so we need more memory. And each list is half the size of the previous one, so our need for memory grows logarithmically as the value of ***n*** increases. 

* ***n***
* ***n/2***
* ***n/4***

## Recursive Depth

Computer scientists favor recursive functions over iterative ones because they tend to use functional languages, where it's important to avoid changing data once it's been passed to a function. 

Recursive functions typically begin with their stopping condition - aka **base case**. The number of times a recursive function calls itself is **recursive depth**. 

The important thing to know is that each programing language has a preference when it comes recursion vs iteration. 

For example, Python is an interpreted language that is very good at iteration. Conversely, it is not good at recursion and has a max recursion depth after which an algorithm stops running. On the other hand, Swift uses something called **tail call optimization** so recursion depth doesn't matter. 

