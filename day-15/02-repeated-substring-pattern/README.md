# Repeated Substring Pattern

## Approach
Checked every possible substring length that divides
the original string length.
Compared each section with the first substring.

## Time Complexity
O(n^2)

## Space Complexity
O(n)

## Edge Case
A string with only one character cannot be formed
by repeating a smaller substring.