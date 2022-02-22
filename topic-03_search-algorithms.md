# Topic 3: Search Algorithms

Say the task is to guess a randomly number (**target**) between 1 and 100 (**range**). After each guess, you're told if it's correct, too high, or too low. This is a **search for a value** problem. This topic briefly describes some of the search algorithms we'll be using to explore Big O. The key takeaway is summarized as:

Algorithm               | Time   | Space
------------------------|--------|-------------
Linear Search           | Linear | Constant
Iterative Binary Search | Binary | Constant
Recursive Binary Search | Binary | Logarithmic

## Linear Search

See `py01_search-linear.py`

With **linear search**, we start with the 1st, 2nd, 3rd values in the list... and continue until we guess correctly or run out of values to compare. Because we're checking the values sequentially, their order doesn't matter - meaning, with linear search, the **list does not need to be sorted**. 

Linear search is also called **sequential search** or **simple search**. A human version of the steps are: 

1. Start with the first value in the list. 
1. Compare value to the target.
1. If they match, task is done.
1. If they don't match, move to the next value and repeat from step 2.
1. If all values have been compared and there is no match, task is done. 

Linear search has a **linear time complexity** - in the worst-case, we need to check every value in the list. 

Linear search has a **constant space complexity** - in the worst-case, we are only working with one list. 

## Iterative Binary Search

See `py02_search-binary.py`

**Binary search** works by starting at the range's midpoint and eliminating ~half the possibilities with each guess. Say range is 1-100 and the target is 63. The first guess is 50, the second guess is 75, the third guess is 63. 

1. Create a pointer to the start and end of the list.
1. Go to the midpoint and compare its value to the target. 
1. If the midpoint value matches the target, algorithm is done.
1. If the midpoint value is less than the target, discard the greater-than half of the range by moving the end pointer to the current midpoint, and repeat from step 2. 
1. If the midpoint value is greater than the target, discard the less-than half of the range by moving the start pointer to the current midpoint, and repeat from step 2. 
1. If the range only has one value remaining and it does not match the target, then the algorithm is done. 

Notice that binary search has a **prerequisite** - **the data set must be sorted**. This is because binary search does not return the target number - it **returns the target's index**, or position, in the list. 

Iterative binary search has a **logarithmic time complexity** - which is any time you see repeated division and elimination by a certain factor (2). 

Iterative binary search has a **constant space complexity** - it works on a single list by using start & end pointers to define the current range. 

## Recursive Binary Search 

See `py03_search_recursive.py`

A **recursive function** is a function that calls itself. It continues to call itself until it has a concrete answer or the stop condition is met. Then it returns the answer back up the chain to the original function. Like iterative binary search, **the list must be sorted**. 

Recursive binary search has a **logarithmic time complexity** - like iterative binary search, it works by eliminating half the range with each guess. 

Recursive binary search has a **logarithmic space complexity** - where iterative binary search uses start and end pointers, recursive search creates a new list with each guess.  

When you compare the Python examples notice that, as written, recursive binary search differs from linear and iterative binary search in that: 

* Can only return True/False + the target's value.
* It cannot return the index of the target. 
* And you cannot track number of operations. 

