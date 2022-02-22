# Topic 5: Inefficient Time Complexities

Inefficient runtimes are algorithms that can't complete in a useful amount of time, so they have little real-world applications. Even so: 

* Recognizing that a part of a problem is unsolvable in a realistic time is a vital skill that lets you move on to other parts that can be solved. 
* Studying these algorithms, we develop strategies that are useful across the board, and can help us make existing algorithms more efficient. 

## O(x^n) - Exponential Runtimes

The **brute force** problem: Imagine you need to open a combo lock with 2 dials. Each dial has the numbers 0-9, for a total of 10 numbers each. 

In the worst case, the algorithm needs to try every combination of 0-9 and 0-9, for a total of 100 combinations. And since the order matters, trying 35 does not eliminate 53. Consider what happens as the number of dials increases:

Dials   | Operations
--------|-------------
O(10^2) | 100 
O(10^3) | 1000
0(10^4) | 10000

This demonstrates why, the longer the password or combination, the better - it quickly becomes impossible for the combo to be cracked in a useful amount of time. 

## O(n!) - Factorial / Combinatorial Runtimes

The **traveling salesman** problem: Given a list of cities, and the distance between each pair of cities, what is the shortest route you can take to visit each city and return to the city of origin? 

To solve this, you need to compare all possible routes. With just 3 cities, it's easy to calculate there are 6 routes. 

```
A-B-C-A
A-C-B-A
B-A-C-B
B-C-A-B
C-A-B-C
C-B-A-C
```

You may think that because A-B-C-A and A-C-B-A are the reverse of each other, that we can eliminate one. But again, we want to model the worst case, and the way roads work in real life, A to B is not always the same distance as B to A. Here's how the number of routes increases as you add cites:  

Cities | Routes
-------|---------------
3!     | 3 * 2 * 1 = 6
4!     | 24
5!     | 120
6!     | 720

