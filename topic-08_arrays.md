# Arrays

Arrays are a fundamental data structure built into almost every programing language. **Arrays** represent a collection of data and are building blocks used to create more complex structures. Each value in an array is represented by an **index** or **key**. 

In fact, in most languages, text is represented as the string type. Under the hood, strings are simply an array of characters stored in a certain order.

Recall that all data structures have 4 common operations - access, search, add, delete. While arrays are efficient at accessing values, they use linear search which we've learned isn't the most efficient. 

## Key Python Points

* Arrays are best represented by the `list` type.
* Arrays are heterogenous - a list can contain multiple data types. 
* Arrays are efficient at accessing data. Arrays are not efficient for search operations.  
* Pointers are stored in equally sized blocks of contiguous memory, while the values are stored elsewhere in memory.
* Python uses amortized memory allocation - the list resize operation allocates multiple blocks at a time following a pattern. 

Operation   | Time     | Space
------------|----------|--------------------
`in` (find) | Linear   | Constant
`insert`    | Linear   | Amortized Constant
`append`    | Constant | Amortized Constant
`extend`    | Constant | Amortized Constant
`pop` value | Linear   | Amortized Constant
`pop` index | Constant | Amortized Constant

## Homogenous and Heterogenous Arrays

Some programing languages - like C, Java, and Swift - use **homogenous arrays** - a given array can only contain the same kind of data. 

Other languages - like Python - use **heterogenous arrays** - a given array can contain multiple kinds of data.  

And in Python, the array is best represented by the `[list]` type. Python does have an array type, but it's something different and we won't be using it here. In data science, a list is very different from an array, and we will be building something called a 'linked list' in the next topic. 

## Contiguous and Non-Contiguous Structures

Arrays are a **contiguous data structure** - the data is stored in blocks of equally sized blocks of memory that are right next to each other, without gaps. Accessing contiguous memory happens in near constant time. 

Link lists are **non-contiguous data structure**, the structure stores a value + a reference/pointer to the memory location for the next value. Following pointers adds to an algorithm's overhead - the runtime of common operations.

## Homogenous Arrays and Contiguous Memory

Languages like C, Swift, and Java use homogenous arrays. Since the type of value stored in the array is known to the language, the compiler can allocate equally sized, contiguous memory to store the VALUES and POINTERS of the array.

## Heterogeneous Arrays and Contiguous Memory

Languages like Python use heterogeneous arrays + pointers. Because the values can be different types and sizes, they aren't suited to contiguous memory. 

Instead, Python uses equally sized, contiguous memory to store the POINTERS ONLY, while the actual values are stores elsewhere in memory. The pointers are all of the same, known data type, so they are suited for contiguous memory.

## More About Contiguous Memory

Every value in an array has a position that is identified by an **index** or key. In most programing languages, indexes are zero-based - meaning the numbering starts 0, 1, 2, 3...

Generally, when an array is declared, a base amount of contiguous memory is allocated as the array's storage. Computers refer to memory by using an **address**. Remember, with a homogeneous array, we are storing values and pointers. With a heterogeneous array we are storing the pointers. 

Because the memory blocks are equally sized and contiguous, the array only needs to store a pointer to the first address - called the **base address**. From there it can follow the pointers to navigate the list sequentially. It can also find any index by using it as an **offset** from the base address.

Say we declare the array: ['dog', 'cat', 'bird', 'fox', 'mouse']. Each value/pointer takes up a certain amount of space in memory called ***M***. 

Now say you want to access 'bird' which is at index [2]. The computer starts at the base address, which is index [0]. It then adds index [2] and multiplies this by the size of ***M*** - this results in the address for 'bird'. This is a simplified example, but is generally how all arrays and contiguous memory work. 

Let's also assume we know how many elements are in the array. So the size of the array is some number called ***N***. From this you know that the array's space = ***N * M***. 

## Amortized Memory

In Python, when you create an empty list, it is allocated ***n+1*** memory - it has room for a single element that isn't being utilized. If you add a single element to the list, you still only need ***n+1*** memory - beyond that, and the size of the memory needs to be reallocated. 

When a list needs more memory, Python calls a **list resize operation** that allocates not just more block, but several more - this way, it doesn't need to call list resize every time a single element is added. The growth pattern is: 0, 4, 8, 16, 25, 35, 46...

In reverse, previously allocated blocks remain until the number of items in the list drops below a growth point and the list resize operation is called. 

