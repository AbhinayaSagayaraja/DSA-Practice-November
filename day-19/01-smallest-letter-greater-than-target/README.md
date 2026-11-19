# Find Smallest Letter Greater Than Target

## Approach
Used binary search on the sorted character list.
If the middle character was smaller than or equal to
the target, searched the right half.

## Time Complexity
O(log n)

## Space Complexity
O(1)

## Edge Case
If no character is greater than the target,
return the first character.