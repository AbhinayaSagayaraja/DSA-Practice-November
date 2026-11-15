# Find the Index of the First Occurrence

## Approach
Used a nested loop to check whether the needle matches
the haystack starting from each possible index.
Returned the first matching index.

## Time Complexity
O(n * m)

## Space Complexity
O(1)

## Edge Case
If the needle is empty, return 0.
If the needle is not found, return -1.