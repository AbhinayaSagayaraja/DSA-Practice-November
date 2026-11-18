# Reorganize String

## Approach
Counted character frequencies using a dictionary.
Used Merge Sort to arrange characters by descending frequency.
Placed the most frequent characters at alternate positions
to prevent identical adjacent characters.

## Time Complexity
O(n + k log k)

## Space Complexity
O(n + k)

## Edge Case
If one character appears more than (n + 1) // 2 times,
a valid arrangement is impossible, so return an empty string.