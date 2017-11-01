# algos-unlocked
Implementation of Algorithms from "Algorithms Unlocked" by Thomas H. Cormen.

### Algorithms:

- Linear search (O(n) time)
- Sentinel Linear search
  - Instead of using the 2n+1 comparisons in linear search, sentinnel linear search only requires n+2 comparisons, by skipping the process of checking whether your index is within valid bounds
- Factorial function
  - Note that both are equally vulnerable to the "RecursionError: maximum recursion depth exceeded in comparison," and that an iterative approach would not suffer from this same issue
- Recursive linear search
  - Note that by way of slicing, this has a memory footprint of n^2/2
