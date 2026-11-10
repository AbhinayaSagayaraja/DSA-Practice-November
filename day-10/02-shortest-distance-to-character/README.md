# Shortest Distance to a Character

## Approach
Used two traversals.
The first traversal calculates distances from the nearest character
on the left. The second traversal updates distances using the nearest
character on the right.

## Time Complexity
O(n)

## Space Complexity
O(n)

## Edge Case
A character located at the current index has distance zero.