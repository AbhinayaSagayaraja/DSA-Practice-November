# Custom Sort String

## Approach
Counted the frequency of each character in s using a dictionary.
Traversed the order string and added characters according to
their required order and frequency.
Added remaining characters at the end.

## Time Complexity
O(n + m + k)

## Space Complexity
O(n + k)

## Edge Case
Characters in s that are not present in order must still
appear in the result.