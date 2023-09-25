# Algorithms specialization - Stanford with Coursera

## Karatsuba multiplication
- [Info](https://mathworld.wolfram.com/KaratsubaMultiplication.html)
- Recursively compute: *ac*
- Recursively compute: *bd*
- Recursively compute: *(a+b)(c+d)*=*ac+bd+ad+bc*
- Gauss’ Trick: *(3)*–*(1)*–*(2)*=*ad*+*bc*

```bash
go run karatsuba_multiplication.go 2147483647 2147483647
> 4611686014132420609
```

## Heap
- Fast way to do repeated minimum computations
- A container for objects that have keys
- Application: event manager
    - object: event records
    - key: time event scheduled to occur
    - extract min: yields the next scheduled event

## Karger min cut
- Input: undirected graph G = (V, E)
- Compute the minimum cut (fewest number of crossing edges) of graph
- While there are more than 2 vertices:
    - pick a remaining edge (u,v) uniformly at random
    - merge (or “contract” ) u and v into a single vertex
    - remove self-loops
    - return cut represented by final 2 vertices

## Counting inversions
- Compute the number of inversions in the file
- Have recursive calls both count inversions and sort
