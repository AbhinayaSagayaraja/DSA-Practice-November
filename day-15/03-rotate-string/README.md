# Rotate String

## Approach
Concatenated the original string with itself.
Checked whether the goal string appears as a substring
using manual character matching.

## Time Complexity
O(n^2)

## Space Complexity
O(n)

## Edge Case
If both strings are empty, return True.
If their lengths differ, return False.