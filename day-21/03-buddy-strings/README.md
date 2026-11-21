# Buddy Strings

## Approach
- First, I check whether both strings have the same length.
- I store the positions where the characters are different.
- If exactly two positions differ, I check whether swapping them makes the strings equal.
- If there are no differences, I check whether a duplicate character exists.

## Time Complexity
O(n), where n is the length of the string.

## Space Complexity
O(n), for storing mismatched positions and character frequencies.

## Edge Case
If both strings are already equal, a swap is possible only if a character appears more than once.