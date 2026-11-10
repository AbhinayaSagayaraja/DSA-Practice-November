# Length of Last Word

## Approach
Traverse the string from the end.
Skip trailing spaces and count characters until the previous space.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Edge Case
If the string contains trailing spaces, they should not be counted.