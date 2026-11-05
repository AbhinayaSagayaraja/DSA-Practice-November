# Count Palindromic Substrings

## Approach
Used the expand-around-center technique.
Considered every character and every gap between characters
as a possible center and expanded while both characters matched.

## Time Complexity
O(n^2)

## Space Complexity
O(1)

## Edge Case
A string with one character contains exactly one palindromic substring.