# Reverse String II

## Approach
Converted the string into a character list.
For every 2k characters, reversed the first k characters
using two pointers.

## Time Complexity
O(n)

## Space Complexity
O(n)

## Edge Case
If the remaining characters are fewer than k,
reverse all the remaining characters.