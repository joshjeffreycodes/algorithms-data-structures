# Topic 4: Efficient Time Complexities: Polynomial Runtimes

Notation      | Complexity 
--------------|--------------
O(n^k)        | Polynomial
O(1)          | Constant 
O(n)          | Linear 
O(log n)      | Logarithmic 
O(log n + 1)  | Binary 
O(n^2)        | Quadratic 
O(n^3)        | Cubic 
O(n log n)    | Quasilinear

![Graph demonstrating efficient Big O complexities](./images/big-o-polynomial.png)

## O(n*k) - Polynomial Runtimes

A polynomial runtime is expressed as O(n^k) where ***k*** is any exponent. Quadratic and cubic runtimes are polynomial. 

If we graph O(n^k) it will have a slope similar to the quadratic runtime seen in the image above. The polynomial slope is the **upper bound** for efficiency. 

Any other slope that falls under this polynomial slope (to the right), is said to be **bound** by it. An **efficient** algorithm is one that either has a Big O value that is polynomial, or has a slope that is bound by a polynomial. 

The image above shows the slopes for efficient runtimes you'll see and use frequently. 

## O(1) - Constant Runtime

In all three search examples, there is a step to read a value in the list. This single step is like a fixed business expense - reading a value costs the same amount each and every time. Operations with a fixed cost have a **constant runtime**.

Note that while the constant slope is not fully bound by the polynomial slope, it is a highly efficient runtime.

## O(n) - Linear Runtime

When, in the worst case, an operation needs to read every value in a list - as with linear search - it has a **linear runtime**. 

Range    | Target | Guesses
---------|--------|---------
1-10     | 10     | 10
1-1000   | 1000   | 1000
1-10000  | 10000  | 10000
1-100000 | 100000 | 100000

## O(log n) - Logarithmic Runtime

When an algorithm repeatedly divides and eliminates data by a certain factor, it has a **logarithmic runtime**. Logarithmic runtime is also referred to as **sublinear** - it always plots below the slope of a linear time operation. Logarithms are the opposite of exponents. 

Exponents multiply: 

* 2^2 = 2 * 2 = 4   
* 2^3 = 2 * 2 * 2 = 8
* 2^4 = 2 * 2 * 2 * 2 = 16

Logarithms divide: 

* log2 4 = 2
* log2 8 = 3
* log2 16 = 4

## O(log2 n + 1) - Binary Runtime

Recall that binary search works by dividing a range in half and eliminating one of those halves with each guess. In other words, it has a logarithmic runtime. And a binary search has the pattern O(log2 n + 1). 

Say ***n*** = 16. The guesses would be 8, 12, 14, 15, 16 - a total of 5 guesses - log2 of 16 + 1 = 5. 

In most cases, we prefer binary over linear search. But for binary search, the data must be sorted. This means that up to a certain value of ***n***, linear search is more performant. 

Range    | Target | Guesses
---------|--------|---------
1-10     | 10     | 4
1-1000   | 1000   | 10
1-10000  | 10000  | 14
1-100000 | 100000 | 17

## O(n^2) - Quadratic Runtime

```
(4,1) (4,2) (4,3) (4,4) 
(3,1) (3,2) (3,3) (3,4) 
(2,1) (2,2) (2,3) (2,4) 
(1,1) (1,2) (1,3) (1,4) 
```
Imagine we need a grid. We pick a random number for the size - say, ***n*** = 4. Because it's a simple example, it's easy to see we want the algorithm to result in a 4x4 grid with 16 cells - ***n^2***. It arrives at 16 coordinates by combining each value of ***n*** with each value of ***n***. Many search algorithms have a worst-case quadratic runtime - more on that later. 

## O(n^3) - Cubic Runtime

A cubic runtime means that, worst-case, the algorithm performs ***n^3*** operations. Cubic runtimes are less common, so no examples will be given. Both quadratic and cubic are **computationally expensive** - small increments of ***n*** result in huge changes to the number of operations carried out. 

## O(n log n) - Quasilinear Runtime

The most common example of **quasilinear runtime** is Merge Sort. It's called quasilinear because it sits above the linear slope (and below the quadratic slope). 

Say we have an unsorted list with the numbers 1-8. The 'Merge' starts by dividing the list in half, then each half in half again, and so on until each list contains a single value. 

This is like binary search where we divide a range in half. More broadly, it's logarithmic. And we know the worst-case of a logarithmic operation is O(log n). 

Then 'Sort' reverses the process in a series of comparison steps. Like linear search, the worst-case requires reading every value in the list. And we know that linear runtime is O(n). 

Together, Merge and Sort have a complexity of O(n log n). 

